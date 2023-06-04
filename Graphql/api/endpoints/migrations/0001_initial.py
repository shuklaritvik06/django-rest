# Generated by Django 4.2.1 on 2023-06-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_name", models.CharField(max_length=100)),
                ("book_desc", models.CharField(max_length=200)),
                ("book_isbn", models.CharField(max_length=25)),
            ],
        ),
    ]