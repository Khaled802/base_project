# Generated by Django 4.1.1 on 2022-10-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0007_tag_posts_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="num_of_likes",
            field=models.IntegerField(default=0),
        ),
    ]
