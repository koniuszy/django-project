from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date
from .models import Book, Author


class BookModelTest(TestCase):
    """Test cases for the Book model."""

    def test_book_creation(self):
        """Test creating a book."""
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            isbn="1234567890123",
            published_date=date(2024, 1, 1),
            description="A test book"
        )
        self.assertEqual(str(book), "Test Book by Test Author")
        self.assertEqual(book.title, "Test Book")


class AuthorModelTest(TestCase):
    """Test cases for the Author model."""

    def test_author_creation(self):
        """Test creating an author."""
        author = Author.objects.create(
            name="John Doe",
            bio="A test author",
            email="john@example.com"
        )
        self.assertEqual(str(author), "John Doe")


class BookAPITest(APITestCase):
    """Test cases for the Book API endpoints."""

    def setUp(self):
        """Set up test data."""
        self.book = Book.objects.create(
            title="API Test Book",
            author="API Author",
            isbn="9876543210123",
            published_date=date(2024, 1, 1)
        )

    def test_list_books(self):
        """Test listing books."""
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        """Test retrieving a single book."""
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "API Test Book")

    def test_create_book(self):
        """Test creating a book via API."""
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'isbn': '1111111111111',
            'published_date': '2024-06-01',
            'description': 'A newly created book'
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)


class AuthorAPITest(APITestCase):
    """Test cases for the Author API endpoints."""

    def setUp(self):
        """Set up test data."""
        self.author = Author.objects.create(
            name="Test Author",
            bio="Test bio"
        )

    def test_list_authors(self):
        """Test listing authors."""
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        """Test creating an author via API."""
        data = {
            'name': 'New Author',
            'bio': 'New author bio',
            'email': 'newauthor@example.com'
        }
        response = self.client.post('/api/authors/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)
