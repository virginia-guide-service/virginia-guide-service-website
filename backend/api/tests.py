from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from datetime import timedelta

from django.utils import timezone

from .models import SpecialtyTourRegistration


class SpecialtyTourRegistrationCaptchaTests(TestCase):
	@patch("api.views.os.getenv", return_value="test-turnstile-secret")
	def test_registration_without_turnstile_token_is_rejected(self, mock_getenv):
		response = APIClient().post(
			"/register-specialty-tour/",
			{
				"first_name": "Test",
				"last_name": "Visitor",
				"email": "test@example.com",
				"phone_number": "555-555-5555",
				"date": (timezone.localdate() + timedelta(days=7)).isoformat(),
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
