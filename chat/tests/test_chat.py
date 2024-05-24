from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from chat.models import ChatRoom


class TestChat(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user_test", password="12456789", email="user_test@tests.com")
        self.http_client = Client()

    def test_home_view_auth(self):
        response = self.http_client.get("/v1/home")
        self.assertIn(response.status_code, [302, 401])
