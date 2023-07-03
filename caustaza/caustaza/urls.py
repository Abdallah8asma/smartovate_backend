"""
URL configuration for caustaza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),                         # URL for Django admin interface
    path("AboutUs/", include("about.urls")),                 # URL for AboutUs app
    path('index/', include('index.urls')),                    # URL for index app
    path('service/', include('service.urls')),                # URL for service app
    path('contact/', include('contact.urls')),                # URL for contact app
    path('team/', include('team.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),     # URL for CKEditor file uploader
    path("schema/", SpectacularAPIView.as_view(), name="schema"),    # URL for API schema
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs")   # URL for Swagger documentation
]

# Serve media files during development when DEBUG is enabled
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
