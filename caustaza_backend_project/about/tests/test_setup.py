from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from about.models import About


class AboutSetup(APITestCase):
    def setUp(self):
        self.index_url = reverse("index")
        self.client = APIClient()

        self.about = About.objects.create(
            title="About",
            subtitle="This is the about page subtitle.",
            meta_title="About meta title",
            meta_description="This is the about page meta description.",
            description="This is the about page description.",
            long_description="This is the about page long description.",
        )
        self.about.save()

    def tearDown(self):
        return super().tearDown()
