from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from contact.models import Contact
from contact.serializers import ContactSerializer
from rest_framework import permissions

# Create your views here.
class CreatecontatcAPIView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer