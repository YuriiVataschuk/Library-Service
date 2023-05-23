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

    class Meta:
        ordering = ["borrow_date"]


class Payment(models.Model):
    class PaymentStatusChoices(models.TextChoices):
        PENDING = "Pending"
        PAID = "Paid"

    class PaymentTypeChoices(models.TextChoices):
        PAYMENT = "Payment"
        FINE = "Fine"

    status = models.CharField(max_length=55, choices=PaymentStatusChoices.choices)
    type = models.CharField(max_length=55, choices=PaymentTypeChoices.choices)
    borrowing_id = models.ForeignKey(Borrowing, on_delete=models.DO_NOTHING)
    session_url = models.URLField()
    session_id = models.IntegerField()
    money_to_pay = models.DecimalField(max_digits=10, decimal_places=2)
