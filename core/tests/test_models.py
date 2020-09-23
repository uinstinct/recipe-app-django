from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Testing to create a new user with email"""
        email = "somehting@testtest.com"
        password = "43@!%#@41"
        user = get_user_model().objects.create_user(
                email=email,
                password=password
            )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_with_email_normalized(self):
        """Test whether the email of the user is normalized"""
        email = 'rwas@FaS.oRg'
        user = get_user_model().objects.create_user(email,'passwordtest')

        self.assertEqual(user.email,email.lower())

    def test_check_user_has_provided_email(self):
        """Test whether the email has been provided by the user"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'noemailProvided')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'mater@recipe.com',
            'mater'
            )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)