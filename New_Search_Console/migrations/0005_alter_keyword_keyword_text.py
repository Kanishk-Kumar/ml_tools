# Generated by Django 4.2.6 on 2023-11-02 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("New_Search_Console", "0004_rename_keyword_keyword_keyword_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="keyword",
            name="keyword_text",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="New_Search_Console.new_query",
            ),
        ),
    ]
