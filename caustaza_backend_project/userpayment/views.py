from django.shortcuts import render
import stripe
from django.views.decorators.csrf import csrf_exempt
from config.settings import base
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
import json
import stripe
from django.core.exceptions import ObjectDoesNotExist

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import Invoice

import requests
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from django.utils import timezone

# Create your views here.




@csrf_exempt
def create_checkout_session(request, price):

    stripe.api_key = base.STRIPE_SECRET_KEY

    try:
       checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": 'USD',
                    "product_data": {
                        "name": "plans",
                    },
                    "unit_amount": int(price),
                },
                "quantity": 1,
            }
        ],

        mode="payment",
        customer_creation='always',
        success_url=base.DOMAIN_NAME,
        cancel_url=base.DOMAIN_NAME,
        )

       return JsonResponse({'success': True, 'checkout_session_id': checkout_session.id})

    except Exception as e:
       return Response(
          {'error': 'somthing went wrong when creating stripe checkout_session' },
          status=status.HTTP_500_INTERNAL_SERVER_ERROR
       )




@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = base.STRIPE_ENDPOINT_SECRET


    #payload = request.body.decode('utf-8')
    payload = request.body
    sig_header = request.headers.get('Stripe-Signature', None)

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('Invalid signature:', e)
        return JsonResponse({'error': 'Invalid signature'}, status=400)

     # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        session = event['data']['object']

        # Retrieve the session ID from the session
        session_id = session['id']
        print('**********',session_id)
        receiptEmail= session['receipt_email']
        print(receiptEmail)
        amount_total = session['amount']
        print('*******',amount_total)
        currency = session['currency']
        print('*******',currency)

        invoice = Invoice(token=session_id, receipt_email=receiptEmail, amount=amount_total,currency=currency)
        invoice.save()
        print("Token saved:", invoice)
        #encode session_id
        token = urlsafe_base64_encode(force_bytes(session_id))
        print("my token is:",token)
#         # Embed the expiration timestamp in the token
        expiration_timestamp = int((timezone.now() + timezone.timedelta(days=1)).timestamp())


        subject = 'Invoice for your purchase'
        body = f'''Thank you for your purchase! Here is your invoice for {amount_total} {currency}
        https://dev.app.smartovate.com/landing-page?token={token}'''
        from_email = 'support@smartovate.com'
        to_email = [receiptEmail]

        email = EmailMessage(
            subject,
            body,
            from_email,
            to_email,
              )
        try:
              email.send()
              print("Email sent successfully")
        except Exception as e:
              print(f"Error sending email: {e}")

    elif event['type'] == 'payment_intent.payment_failed':
        # Handle payment failures
        session = event['data']['object']
        customer_email = session.get('customer_email', None)


        if customer_email:
            # Send an email to the customer about the payment failure
            subject = 'Payment Failed for Your Purchase'
            body = 'We regret to inform you that your payment has failed. Please check your payment details and try again.'
            from_email = 'hajer.boukhari@caustaza.com'
            to_email =session['receipt_email']

            email = EmailMessage(
            subject,
            body,
            from_email,
            to_email,
        )
        email.send()

    return HttpResponse(status=200)

@csrf_exempt
def webhook(request, received_token):
    try:
        # Decode the received token

        decoded_token = urlsafe_base64_decode(received_token)
        decoded_token_str = decoded_token.decode()



        # Retrieve the invoice using the decoded token
        invoice = Invoice.objects.get(token=decoded_token_str)

        #Prepare the response data
        response_data = {
            'success': True,
            'message': 'Token is valid',
            'receipt_email': invoice.receipt_email,
            'amount_total': invoice.amount,
            'currency': invoice.currency,
        }

        return JsonResponse(response_data)

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=400)

