# Generated by Django 4.1.2 on 2022-12-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="resources",
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
                ("class_title", models.CharField(max_length=5)),
                ("resource_name", models.CharField(max_length=50)),
                ("link", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "resources",
            },
        ),
    ]
