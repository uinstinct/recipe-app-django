from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

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

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string respresentation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)