from django.db import models
from django.utils import timezone
from rest_framework import serializers

from books.models import Book
from books.serializers import BookListSerializer
from borrowings.models import Borrowing


class BorrowingDetailSerializer(serializers.ModelSerializer):
    book = BookListSerializer(many=False, read_only=True)
    borrow_date = serializers.DateField(read_only=True)
    expected_return_date = serializers.DateField(read_only=True)

    class Meta:
        model = Borrowing
        exclude = ("user",)


class BorrowingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        exclude = ("actual_return_date", "user")

    def create(self, validated_data):
        book = validated_data["book"]
        if book.inventory == 0:
            raise serializers.ValidationError("Book is out of stock.")

        book.inventory -= 1
        book.save()

        borrowing = Borrowing.objects.create(**validated_data)
        return borrowing


class BorrowingReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ("id",)

    def validate(self, attrs):
        borrowing = self.instance

        if borrowing.actual_return_date:
            raise serializers.ValidationError("Borrowing has already been returned.")

        borrowing.actual_return_date = timezone.now().date()
        borrowing.save()

        book = Book.objects.filter(id=borrowing.book.pk)
        book.update(inventory=models.F("inventory") + 1)

        return attrs
