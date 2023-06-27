from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from caustaza.utils import translate_data
from .serializers import *
from .models import *


class PageindexListView(ListAPIView):
    queryset = Pageindex.objects.all()
    serializer_class = PageindexSerializer
    pagination_class = None

    def get(self, request):
        language = request.query_params.get('language', 'en')  # Default language is English ('en')

        # Retrieve all page indexes from the database
        page_indexes = self.get_queryset()

        # Translate the page indexes to the desired language
        translated_page_indexes = translate_data(page_indexes)

        # Return the translated page indexes as JSON response
        return Response({'page_indexes': translated_page_indexes})


class FeedbackClientListView(ListAPIView):
    queryset = FeedbackClient.objects.all()[:3]
    serializer_class = FeedbackSerializer
    pagination_class = None

    def get(self, request):
        language = request.query_params.get('language', 'en')  # Default language is English ('en')

        # Retrieve all feedback clients from the database
        feedback_clients = self.get_queryset()

        # Translate the feedback clients to the desired language
        translated_feedback_clients = translate_data(feedback_clients)

        # Return the translated feedback clients as JSON response
        return Response({'feedback_clients': translated_feedback_clients})