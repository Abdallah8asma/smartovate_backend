from django.urls import path, include
from . import views

urlpatterns = [
     path("create/contact/", views.CreatecontatcAPIView.as_view(), name="contact"),
]