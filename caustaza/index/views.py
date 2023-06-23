from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.response import Response
from translate import Translator
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
        target_languages = ['fr', 'en', 'de']  # French, English, and German languages
        translated_page_indexes = []
        for page_index in page_indexes:
            translated_data = {}
            for field in page_index._meta.fields:
                field_name = field.name
                field_value = getattr(page_index, field_name)
                if isinstance(field_value, (int, float)):
                    translated_data[field_name] = field_value
                else:
                    translated_data[field_name] = {}
                    for language in target_languages:
                        translator = Translator(to_lang=language)
                        translated_field_value = translator.translate(str(field_value))
                        translated_data[field_name][language] = translated_field_value
            translated_page_indexes.append(translated_data)

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
        target_languages = ['fr', 'en', 'de']  # French, English, and German languages
        translated_feedback_clients = []
        for feedback_client in feedback_clients:
            translated_data = {}
            for field in feedback_client._meta.fields:
                field_name = field.name
                field_value = getattr(feedback_client, field_name)
                if isinstance(field_value, (int, float)) :
                    translated_data[field_name] = field_value
                else:
                    translated_data[field_name] = {}
                    for language in target_languages:
                        try:
                            translator = Translator(to_lang=language)
                            translated_field_value = translator.translate(str(field_value))
                            translated_data[field_name][language] = translated_field_value
                        except UnicodeDecodeError:
                            # Handle the UnicodeDecodeError, for example, by providing a default value
                            translated_data[field_name][language] = 'Translation not available'
            translated_feedback_clients.append(translated_data)

        # Return the translated feedback clients as JSON response
        return Response({'feedback_clients': translated_feedback_clients})

class CreatenewsletterAPIView(CreateAPIView):
    queryset = newsletter.objects.all()
    serializer_class = NewsletterSerializer
