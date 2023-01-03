import unittest

from django.test import TestCase

from .models import Url


class ViewTests(TestCase):
    def setUp(self):
        self.url = Url.objects.create(full_url="https://www.google.com", short_url="12345678")
        self.expired_url = Url.objects.create(full_url="https://www.google.com", short_url="87654321", is_active=False)

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_url_result(self):
        response = self.client.post("/url_result", {"url": "localhost:8000", "short_url": "12345678"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "url_result.html")

    def test_redirect_view(self):
        response = self.client.get("/12345678")
        self.assertEqual(response.status_code, 302)

    def test_redirect_view_url_inactive(self):
        response = self.client.get("/87654321")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
