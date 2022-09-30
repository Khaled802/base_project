# Generated by Django 4.1.1 on 2022-09-29 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("details", models.TextField()),
                ("picture", models.ImageField(upload_to="images/")),
                ("created_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
