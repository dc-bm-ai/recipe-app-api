from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Class to test user model"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email successful"""
        email = 'abc@gmail.com'
        password = 'testPassword123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_email(self):
        """Validate that email id is provided"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "pass123")
