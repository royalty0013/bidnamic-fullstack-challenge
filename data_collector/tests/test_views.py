from urllib import response
from django.test import TestCase, Client
from data_collector.forms import DataCollectorForm
from user_auth.forms import RegisterForm
from django.contrib.auth.models import User
from django.urls import reverse

class RegisterFormTestCase(TestCase):
    def setUp(self):
        self.first_name = "Hassan"
        self.last_name = "Braimah"
        self.username = "royalty0013"
        self.email = "royalty0013@gmail.com"
        self.password = "justtestpass"

    def test_register_route(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='user_auth/register.html')

    def test_register_form(self):
        response = self.client.post(reverse("user_auth:register"), data={
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email,
            "password1": self.password,
            "password2": self.password
        })
        self.assertEqual(response.status_code,200)