# Generated by Django 4.2.6 on 2023-11-01 09:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("New_Search_Console", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="keyword",
            old_name="question",
            new_name="keyword",
        ),
    ]