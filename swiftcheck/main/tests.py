from django.test import TestCase
from django.urls import reverse

from .models import Course, User


class CorsTests(TestCase):
    def setUp(self):
        teacher = User.objects.create(
            username="teacher",
            email="teacher@example.com",
            password="Password123!",
        )
        Course.objects.create(
            name="React Basics",
            description="Intro course",
            price=99,
            teacher=teacher,
            category="FRONTEND",
        )

    def test_api_courses_allows_vite_origin(self):
        response = self.client.get(
            reverse("api_courses"),
            HTTP_ORIGIN="http://localhost:5173",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Access-Control-Allow-Origin"],
            "http://localhost:5173",
        )
        self.assertEqual(response["Access-Control-Allow-Credentials"], "true")

    def test_preflight_options_allows_vite_origin(self):
        response = self.client.options(
            reverse("api_courses"),
            HTTP_ORIGIN="http://localhost:5173",
            HTTP_ACCESS_CONTROL_REQUEST_METHOD="GET",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Access-Control-Allow-Origin"],
            "http://localhost:5173",
        )
