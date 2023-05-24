from django.test import TestCase, RequestFactory
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAdminUser
from books.models import Book
from books.views import BookListViewSet


class BookListViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = BookListViewSet.as_view({"get": "list", "post": "create"})
        self.book1 = Book.objects.create(
            title="Book 1", author="Author 1", daily_fee=2.99, inventory=10
        )
        self.book2 = Book.objects.create(
            title="Book 2", author="Author 2", daily_fee=4.99, inventory=10
        )
        self.book3 = Book.objects.create(
            title="Book 3", author="Author 1", daily_fee=6.99, inventory=10
        )

    def test_list_books_with_no_filters(self):
        request = self.factory.get("/books/")
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)  # Ensure all books are returned

    def test_list_books_with_title_filter(self):
        request = self.factory.get("/books/", {"title": "Book 1"})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Ensure only one book is returned
        self.assertEqual(response.data[0]["title"], "Book 1")

    def test_list_books_with_authors_filter(self):
        request = self.factory.get("/books/", {"authors": "Author 1"})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Ensure two books are returned
        self.assertEqual(response.data[0]["author"], "Author 1")
        self.assertEqual(response.data[1]["author"], "Author 1")

    def test_list_books_with_daily_fee_filter(self):
        request = self.factory.get("/books/", {"daily_fee": "2.99,6.99"})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Ensure two books are returned
        self.assertEqual(response.data[0]["daily_fee"], "2.99")
        self.assertEqual(response.data[1]["daily_fee"], "6.99")

    def test_list_books_permissions(self):
        request = self.factory.get("/books/")

        view = BookListViewSet()
        view.request = request
        view.action = "list"
        permissions = view.get_permissions()
        self.assertEqual(len(permissions), 1)
        self.assertIsInstance(permissions[0], AllowAny)

        request = self.factory.post("/books/")
        view = BookListViewSet()
        view.request = request
        view.action = "create"
        permissions = view.get_permissions()
        self.assertEqual(len(permissions), 1)
        self.assertIsInstance(permissions[0], IsAdminUser)
