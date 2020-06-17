from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating new user successful
        :return:
        """
        email = 'test@email.com'
        password = "Testpass123"
        user = get_user_model().objects().create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.checkPassword(password))
