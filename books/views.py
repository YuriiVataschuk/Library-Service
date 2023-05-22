from django.shortcuts import render
from rest_framework import viewsets

from books.models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
