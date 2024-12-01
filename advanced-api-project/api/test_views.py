from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book
from rest_framework.permissions import IsAuthenticated


class BookAPITestCase(APITestCase):

    def setUp(self):
        """
        Set up the test environment.
        Create test user, authenticate, and create sample book data.
        """
        self.user = User.objects.create_user(username='testuser', password='password')
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2024
        }
        self.book = Book.objects.create(**self.book_data)
        self.url_list = '/api/books/'
        self.url_detail = f'/api/books/{self.book.id}/'
        self.client.login(username='testuser', password='password')

    def test_create_book(self):
        """Test the creation of a book."""
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2024
        }
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author'], data['author'])
        self.assertEqual(response.data['publication_year'], data['publication_year'])

    def test_retrieve_books(self):
        """Test retrieving a list of books."""
        response = self.client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure at least one book is returned

    def test_retrieve_single_book(self):
        """Test retrieving a single book."""
        response = self.client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        """Test updating an existing book."""
        data = {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publication_year': 2025
        }
        response = self.client.put(self.url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, data['title'])
        self.assertEqual(self.book.author, data['author'])
        self.assertEqual(self.book.publication_year, data['publication_year'])

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Ensure that the book is deleted
        self.assertEqual(Book.objects.count(), 0)

    def test_permissions_for_create(self):
        """Test that creating a book is restricted to authenticated users."""
        self.client.logout()
        data = {
            'title': 'Another Book',
            'author': 'Another Author',
            'publication_year': 2024
        }
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_books(self):
        """Test searching books by title or author."""
        response = self.client.get(self.url_list, {'search': 'Test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Ensure some books match the search query

    def test_filter_books(self):
        """Test filtering books by title, author, and publication year."""
        response = self.client.get(self.url_list, {'title': 'Test Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering_books(self):
        """Test ordering books by title or publication year."""
        response = self.client.get(self.url_list, {'ordering': 'title'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]['title'] <= response.data[-1]['title'])
