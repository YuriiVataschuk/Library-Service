from django.db import models


class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "Hard"
        SOFT = "Soft"

    title = models.CharField(unique=True, max_length=255)
    author = models.CharField(max_length=255)
    Cover = models.CharField(choices=CoverChoices.choices)
    inventory = models.IntegerField()
    daily_fee = models.DecimalField()
