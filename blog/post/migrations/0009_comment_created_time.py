# Generated by Django 4.1.1 on 2022-10-06 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0008_post_num_of_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]