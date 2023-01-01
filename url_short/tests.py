from django.test import TestCase


class ViewTests(TestCase):
    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_url_result(self):
        response = self.client.post("/url_result", {"url": "localhost:8000", "short_url": "12345678"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "url_result.html")

    def test_redirect_view(self):
        response = self.client.get("/5e988346f3b4ba8e")
        self.assertEqual(response.status_code, 302)
