from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class MyModelAPITestCase(APITestCase):
    def test_get_all_models(self):
        url = reverse("home_page")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
