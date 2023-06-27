from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from contact.models import Contact
from contact.serializers import ContactSerializer

# Create your views here.
class CreatecontatcAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer