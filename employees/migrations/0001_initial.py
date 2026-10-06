# Generated manually for the Magnus employee assignment.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("first_name", models.CharField(max_length=80)),
                ("last_name", models.CharField(max_length=80)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("mobile_number", models.CharField(max_length=15)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")],
                        default="Male",
                        max_length=10,
                    ),
                ),
                ("address", models.TextField(blank=True)),
                ("country", models.CharField(default="India", max_length=80)),
                ("city", models.CharField(blank=True, max_length=80)),
                ("other_city", models.BooleanField(default=False)),
                ("skills", models.CharField(blank=True, max_length=500)),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="employees/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-id"]},
        ),
    ]
