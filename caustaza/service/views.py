from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from caustaza.utils import translate_data
from .serializers import *
from .models import *

class ServicesIndexListView(ListAPIView):
    queryset = Services.objects.all().filter(page_index_published=True)
    serializer_class = ServicesSerializer
    pagination_class = None

    def get(self, request):
        language = request.query_params.get('language', 'en')  # Default language is English ('en')

        # Retrieve all services from the database
        services = self.get_queryset()

        # Translate the services to the desired language
        translated_services = translate_data(services)

        # Return the translated services as JSON response
        return Response({'services': translated_services})


class ServicesListView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    pagination_class = None

    def get(self, request):
        language = request.query_params.get('language', 'en')  # Default language is English ('en')

        # Retrieve all services from the database
        services = self.get_queryset()

        # Translate the services to the desired language
        translated_services = translate_data(services)

        # Return the translated services as JSON response
        return Response({'services': translated_services})


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = None

    def get(self, request):
        language = request.query_params.get('language', 'en')  # Default language is English ('en')

        # Retrieve all services from the database
        services = self.get_queryset()

        # Translate the services to the desired language
        translated_services = translate_data(services)

        # Return the translated services as JSON response
        return Response({'services': translated_services})