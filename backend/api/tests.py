from django.test import TestCase
from rest_framework.test import APIClient

from .models import SpecialtyTourRegistration


class SpecialtyTourRegistrationCaptchaTests(TestCase):
	def test_registration_without_turnstile_token_is_rejected(self):
		response = APIClient().post(
			"/register-specialty-tour/",
			{
				"first_name": "Test",
				"last_name": "Visitor",
				"email": "test@example.com",
				"phone_number": "555-555-5555",
				"date": "2026-09-05",
				"time": "11:00",
				"guests": 1,
				"minors": 0,
				"tour_type": "Standard Historical",
				"notes": "",
			},
			format="json",
		)

		self.assertEqual(response.status_code, 400)
		self.assertIn("captcha", response.data)
		self.assertEqual(SpecialtyTourRegistration.objects.count(), 0)
