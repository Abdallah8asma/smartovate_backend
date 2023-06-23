from django.urls import path, include
from .views import PageindexListView, FeedbackClientListView, CreatenewsletterAPIView

urlpatterns = [
    path("newsletter/", CreatenewsletterAPIView.as_view(), name="newsletter"), 
    path("Pageindex/", PageindexListView.as_view(), name="Pageindex"),
    path("feedbackclient/", FeedbackClientListView.as_view(), name="feedbackclient"),
]
