from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from caustaza_backend_project.about.views import AboutViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


app_name = "api"
router.register(r"about", AboutViewSet, basename="about")
urlpatterns = router.urls
