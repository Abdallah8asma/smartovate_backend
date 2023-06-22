from django.shortcuts import render

from .serializers import FeaadbackSerializer, NewsletterSerializer, PageindexSerializer

from .models import FeedbackClient, Pageindex, newsletter
from rest_framework.generics import CreateAPIView, ListAPIView
# Create your views here.

class pageIndexListView(ListAPIView):
    queryset = Pageindex.objects.all()
    serializer_class = PageindexSerializer
    pagination_class = None


class FeedbackClienListView(ListAPIView):
    queryset = FeedbackClient.objects.all()[:3]
    serializer_class = FeaadbackSerializer
    pagination_class = None

class CreatenewsletterAPIView(CreateAPIView):
    queryset = newsletter.objects.all()
    serializer_class = NewsletterSerializer
