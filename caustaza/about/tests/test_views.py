from rest_framework import status
from .test_setup import AboutSetup


class TestViews(AboutSetup):
    """Test views for About app."""

    def test_about_page(self):
        """Test that the about page apis are working with the correct data."""

        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "About")

        self.assertEqual(response.data[0]["title"], "About")
        self.assertEqual(
            response.data[0]["subtitle"], "This is the about page subtitle."
        )
        self.assertEqual(response.data[0]["meta_title"], "About meta title")
        self.assertEqual(
            response.data[0]["meta_description"],
            "This is the about page meta description.",
        )
        self.assertEqual(
            response.data[0]["description"], "This is the about page description."
        )
        self.assertEqual(
            response.data[0]["long_description"],
            "This is the about page long description.",
        )
