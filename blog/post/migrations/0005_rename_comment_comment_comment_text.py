# Generated by Django 4.1.1 on 2022-10-01 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0004_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="comment", new_name="comment_text",
        ),
    ]