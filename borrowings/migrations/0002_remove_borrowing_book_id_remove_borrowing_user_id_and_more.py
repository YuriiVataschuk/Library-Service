# Generated by Django 4.2.1 on 2023-05-24 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("books", "0002_alter_book_options_alter_book_cover_and_more"),
        ("borrowings", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="borrowing",
            name="book_id",
        ),
        migrations.RemoveField(
            model_name="borrowing",
            name="user_id",
        ),
        migrations.AddField(
            model_name="borrowing",
            name="book",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="books.book",
            ),
        ),
        migrations.AddField(
            model_name="borrowing",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Payment",
        ),
    ]