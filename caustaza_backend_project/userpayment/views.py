from django.shortcuts import render,redirect
import stripe
from django.views.decorators.csrf import csrf_exempt
from config.settings import base
from django.http import HttpResponseRedirect ,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
import json
import stripe


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import stripe
from .models import Invoice

import requests

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
                    "unit_amount": int(price) * 100,
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

        # Retrieve the session ID stored in the session
        # stored_session_id = request.session.get('id', None)

        # if stored_session_id == session_id:
            # Send an invoice to the customer's email
        customer_email = session['receipt_email']
        print('*******',customer_email)
        amount_total = session['amount']
        print('*******',amount_total)
        currency = session['currency']
        print('*******',currency)

        #encode session_id
        session_idencoded=session_id.encode()

        #Store the encoded session_id in the database
        invoice = Invoice(session_idencoded)
        invoice.save()

        subject = 'Invoice for your purchase'
        body = f'''Thank you for your purchase! Here is your invoice for {amount_total} {currency}
        https://dev.app.smartovate.com/landing-page?token={session_idencoded}'''
        from_email = 'hajer.boukhari@caustaza.com'
            #lazem:encodih
            #formedepersistance
        to_email = [customer_email]

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
def webhook(request):
    token_from_request = request.GET.get('token').decode()

    if token_from_request is not None:
        try:
          token_existing = Invoice.objects.get(stored_session_id=token_from_request)

          customer_email = token_existing['customer_email']
          amount_total = token_existing['amount_total']
          currency = token_existing['currency']

          response_data = {
                'success': True,
                'message': 'Token is valid',
                'customer_email': customer_email,
                'amount_total': amount_total,
                'currency': currency,
            }

          return JsonResponse(response_data)

        except Invoice.DoesNotExist:

            return JsonResponse({'error': 'Invalid token'}, status=400)
    else:

        return JsonResponse({'error': 'Token is missing from the request'}, status=400)


