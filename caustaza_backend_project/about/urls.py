from django.urls import path
from .views import AboutListView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name = "about"
urlpatterns = [
    path("", AboutListView.as_view(), name="index"),
    # Optional UI:
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
