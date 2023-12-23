from django.shortcuts import render,redirect
import stripe
from django.views.decorators.csrf import csrf_exempt
from config.settings import base
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
# Create your views here.







@csrf_exempt
def checkout_session(request, price, currency):
    if request.method=='POST':

     stripe.api_key = base.STRIPE_SECRET_KEY

    try:
       checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": currency,
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
       return redirect(checkout_session.url, code=303)

    except Exception as e:
       return Response(
          {'error': 'somthing went wrong when creating stripe checkout_session' },
          status=status.HTTP_500_INTERNAL_SERVER_ERROR
       )

