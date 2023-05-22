from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "Hard"
        SOFT = "Soft"

    title = models.CharField(unique=True, max_length=255)
    author = models.CharField(max_length=255)
    Cover = models.CharField(
        max_length=4,
        choices=CoverChoices.choices
    )
    inventory = models.IntegerField(validators=(MinValueValidator(1),))
    daily_fee = models.DecimalField(max_digits=55, decimal_places=2)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} (authors: {self.author})"
