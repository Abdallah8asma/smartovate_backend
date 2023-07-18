from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from caustaza_backend_project.about.views import AboutViewSet
from caustaza_backend_project.jobs.views import JobsViewSet
from caustaza_backend_project.services.views import ServiceViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


app_name = "api"

router.register(r"services", ServiceViewSet, basename="services")
router.register(r"about", AboutViewSet, basename="about")
router.register(r"jobs", JobsViewSet, basename="jobs")

urlpatterns = router.urls
