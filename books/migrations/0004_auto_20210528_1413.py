# Generated by Django 2.2.7 on 2021-05-28 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('read_all_books', 'Can read all books')]},
        ),
    ]
