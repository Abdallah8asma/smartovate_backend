from django.urls import path, include
from . import views

urlpatterns = [
     path("newsletter/", views.CreatenewsletterAPIView.as_view(), name="newsletter"), 
     path("Pageindex/", views.pageIndexListView.as_view(), name="Pageindex"),
     path("feedbackclient/", views.FeedbackClienListView.as_view(), name="feedbackclient"),
]