from django.db import models


class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "Hard"
        SOFT = "Soft"

    title = models.CharField(unique=True, max_length=255)
    author = models.CharField(max_length=255)
    Cover = models.CharField(max_length=255, choices=CoverChoices.choices)
    inventory = models.IntegerField()
    daily_fee = models.DecimalField(max_digits=55, decimal_places=2)
