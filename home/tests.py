from django.test import TestCase
from wagtail.models import Page
from .models import HomePage, BlogPage, BlogIndexPage


class HomePageTest(TestCase):
    """Test cases for Wagtail page models."""

    def test_homepage_model_exists(self):
        """Test that HomePage model is properly defined."""
        self.assertTrue(issubclass(HomePage, Page))

    def test_blogpage_model_exists(self):
        """Test that BlogPage model is properly defined."""
        self.assertTrue(issubclass(BlogPage, Page))

    def test_blogindexpage_model_exists(self):
        """Test that BlogIndexPage model is properly defined."""
        self.assertTrue(issubclass(BlogIndexPage, Page))
