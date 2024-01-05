
# https://dev.app.smartovate.com/landing-page
# https://dev.app.smartovate.com/management/api/lp/webhook
# import requests
# https://dev.app.smartovate.com/landing-page?token=.....

# from django.core.mail import EmailMessage

# email = EmailMessage(
#             subject,
#             body,
#             from_email,
#             to_email,
#         )
#         email.send()


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.eu.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_HOST_USER = 'postmaster@smartovate.com'
# EMAIL_HOST_PASSWORD = ...
# EMAIL_DEBUG = True  # Enable debugging
# DEFAULT_FROM_EMAIL = 'postmaster@smartovate.com'
# support@smartovate.com

# EMAIL_SUBJECT_PREFIX = 'mail'


# from django.core.mail import EmailMessage

# email = EmailMessage(
#             subject,
#             body,
#             from_email,
#             to_email,
#         )
#         email.send()


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.eu.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_HOST_USER = 'postmaster@smartovate.com'
# EMAIL_HOST_PASSWORD = ...
# EMAIL_DEBUG = True  # Enable debugging
# DEFAULT_FROM_EMAIL = 'postmaster@smartovate.com'
# EMAIL_SUBJECT_PREFIX = 'mail'

# uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
#         # Embed the expiration timestamp in the token
#         expiration_timestamp = int((timezone.now() + timezone.timedelta(days=1)).timestamp())
#         token = f"{default_token_generator.make_token(user)}-{expiration_timestamp}"

#         reset_password_link = (
#             f"{settings.BASE_URL}/reset-password?uidb64={uidb64}&token={token}"
#         )

#         email_subject = "Reset Password"
#         email_body = render_to_string(
# email = EmailMessage(
#             email_subject,
#             email_body,
#             "support@smartovate.com",
#             [receiver_email],
#             reply_to=["support@caustaza.com"]
#         )

#         email.send()

# email_body = render_to_string(
#             "reset_password_email.html",
#             {
#                 "user": user,
#                 "reset_password_link": reset_password_link,
#                 "domain": f"{settings.BASE_URL}",
#             },
#         )


# return Response({'detail': checkout.url})



# line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'usd',
#                         'unit_amount': amount,
#                         'product_data': {
#                             'name': 'My product',
#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#         )
# amount = int(request.POST['amount'])
