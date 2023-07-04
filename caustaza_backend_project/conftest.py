import pytest

from caustaza_backend_project.about.models import About
from caustaza_backend_project.About.tests.factories import AboutFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def about(db) -> About:
    return AboutFactory()
