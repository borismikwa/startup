# Generated by Django 4.1.5 on 2023-01-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0004_alter_service_service_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="img/services/"),
        ),
    ]
