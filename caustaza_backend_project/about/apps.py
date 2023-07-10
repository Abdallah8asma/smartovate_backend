from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AboutConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "caustaza_backend_project.about"
    verbose_name = _("About")

    def ready(self):
        try:
            import caustaza_backend_project.about.signals  # noqa: F401
        except ImportError:
            pass
