from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


class AuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user_test", password="12456789", email="user_test@tests.com")
        self.http_client = Client()

    def test_login(self):
        response = self.http_client.post("/auth/v1/login/", {"username": self.user.username, "password": user.password})
        self.assertEqual(response.status_code, 200)
        self.http_client.force_login(self.user)
        response = self.http_client.get("/v1/home")
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        http_client = Client()
        user = User(username="user_test", password="12456789", email="user_test@tests.com")
        response = http_client.post("/auth/v1/login/", {"username": user.username, "password": user.password})
        self.assertEqual(response.status_code, 200)
        response = http_client.post("/auth/v1/logout/", {})
        self.assertEqual(response.status_code, 200)
        response = http_client.get("/v1/home/", {})
        self.assertEqual(response.content, b"Live Chat Login.")