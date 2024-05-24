from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


class AuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user_test", password="12456789", email="user_test@tests.com")
        self.http_client = Client()

    def test_login(self):
        response = self.http_client.post("/auth/v1/login/",
                                         {"username": self.user.username, "password": self.user.password})
        self.assertEqual(response.status_code, 200)
        self.http_client.force_login(self.user)
        response = self.http_client.get("/v1/home")
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.http_client.post("/auth/v1/login/",
                                         {"username": self.user.username, "password": self.user.password})
        self.assertEqual(response.status_code, 200)
        self.http_client.force_login(self.user)
        response = self.http_client.post("/auth/v1/logout/", {})
        self.assertIn(response.status_code, [302, 401])
        response = self.http_client.get("/v1/home", {})
        self.assertIn(response.status_code, [302, 401])

    def test_create_user_invalid_form(self):
        new_username = "new_username"
        new_email = "nw@test.com"
        response_get = self.http_client.get("/auth/v1/sign_up")
        self.assertEqual(response_get.status_code, 200)
        self.http_client.post("/auth/v1/sign_up",
                              {"username": new_username,
                               "password": self.user.password
                               })

        user_name_found = User.objects.filter(username=new_username).count()
        self.assertEqual(user_name_found, 0)
        response = self.http_client.post("/auth/v1/sign_up",
                                         {
                                             "email": new_email,
                                             "username": new_username,
                                             "first_name": "First name test",
                                             "last_name": "Last name test",
                                             "password1": "20532050aA",
                                             "password2": "20532050a",
                                         })
        self.assertIn(response.status_code, [200, 401])
        user_name_found = User.objects.filter(username=new_username).count()
        self.assertEqual(user_name_found, 0)

    def test_create_user(self):
        new_username = "new_username"
        new_email = "nw@test.com"
        response_get = self.http_client.get("/auth/v1/sign_up")
        self.assertEqual(response_get.status_code, 200)
        self.http_client.post("/auth/v1/sign_up",
                              {"username": new_username,
                               "password": self.user.password
                               })

        user_name_found = User.objects.filter(username=new_username).count()
        self.assertEqual(user_name_found, 0)
        response = self.http_client.post("/auth/v1/sign_up",
                                         {
                                             "email": new_email,
                                             "username": new_username,
                                             "first_name": "First name test",
                                             "last_name": "Last name test",
                                             "password1": "20532050aA",
                                             "password2": "20532050aA",
                                         })

        self.assertIn(response.status_code, [302, 401])
        user_name_found = User.objects.filter(username=new_username).count()
        self.assertEqual(user_name_found, 1)
