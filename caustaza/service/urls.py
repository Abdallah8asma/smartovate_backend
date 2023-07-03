from django.urls import path
from .views import ServicesIndexListView,ServicesListView,ServiceListView

urlpatterns = [
    path('', ServiceListView.as_view()),
    path('services/', ServicesListView.as_view()),
    path('servicesIndex/', ServicesIndexListView.as_view()),
 
]
