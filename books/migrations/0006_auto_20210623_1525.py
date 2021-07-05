# Generated by Django 2.2.7 on 2021-06-23 15:25

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0005_auto_20210603_1537"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="author",
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("birthday", models.DateField(blank=True, null=True)),
                ("website", models.CharField(max_length=200)),
                ("biography", models.TextField()),
                (
                    "books",
                    models.ManyToManyField(blank=True, related_name="author_book", to="books.Book"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(to="books.Author"),
        ),
    ]
