# Generated by Django 5.0.3 on 2024-03-28 13:08

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Donating",
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
                ("donarName", models.CharField(max_length=50)),
                ("age", models.IntegerField(validators=[core.models.validate_min_age])),
                (
                    "donarBloodGroup",
                    models.CharField(
                        choices=[
                            ("A+", "A +ve"),
                            ("A-", "A -ve"),
                            ("B+", "B +ve"),
                            ("B-", "B -ve"),
                            ("O+", "O +ve"),
                            ("O-", "O -ve"),
                            ("AB+", "AB +ve"),
                            ("AB-", "AB -ve"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        max_length=10,
                    ),
                ),
                ("identity", models.ImageField(upload_to="donarID")),
            ],
        ),
    ]
