
from django.urls import path
from .views import UsersViewSet

app_name = "usersapp"

urlpatterns = [
    path('register/', UsersViewSet.as_view({'post': 'create'}), name='create'),
]
