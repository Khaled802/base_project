# Generated by Django 4.1.1 on 2022-10-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_alter_customuser_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="picture",
            field=models.ImageField(default="default.bng", upload_to="images/"),
        ),
    ]
