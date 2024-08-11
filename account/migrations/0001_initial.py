# Generated by Django 4.2.15 on 2024-08-09 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("bio", models.TextField(blank=True)),
                ("github_url", models.URLField(blank=True, max_length=2000)),
                ("linkedin_url", models.URLField(blank=True, max_length=2000)),
                ("twitter_url", models.URLField(blank=True, max_length=2000)),
                ("website_url", models.URLField(blank=True, max_length=2000)),
                ("photo", models.ImageField(blank=True, upload_to="users/%Y/%m/%d/")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
