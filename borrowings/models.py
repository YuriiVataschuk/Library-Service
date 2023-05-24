from django.db import models

from books.models import Book


class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(blank=True, null=True)
    book_id = models.ForeignKey(
        Book,
        on_delete=models.DO_NOTHING,
        related_name="book_id"
    )
    user_id = models.ForeignKey(
        Book,
        on_delete=models.DO_NOTHING,
        related_name="user_id"
    )
