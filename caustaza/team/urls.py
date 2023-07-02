from django.urls import path
from .views import TeamListView, TeamMemberListView

urlpatterns = [
    path('', TeamListView.as_view()),
    path('teammember/', TeamMemberListView.as_view()),
]
