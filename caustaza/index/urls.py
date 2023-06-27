from django.urls import path, include
from .views import PageindexListView, FeedbackClientListView

urlpatterns = [
    
    path("Pageindex/", PageindexListView.as_view(), name="Pageindex"),
    path("feedbackclient/", FeedbackClientListView.as_view(), name="feedbackclient"),
]
