# Generated by Django 4.1.5 on 2023-01-18 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="short_service",
            field=models.CharField(default="Not set", max_length=150),
            preserve_default=False,
        ),
    ]
