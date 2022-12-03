# Generated by Django 4.1.3 on 2022-12-03 04:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Auto",
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
                ("auto_name", models.CharField(max_length=50)),
                (
                    "auto_price",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sale",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Specs",
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
                ("spec_name", models.CharField(max_length=50)),
                ("value", models.CharField(max_length=50)),
                (
                    "spec",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fset.auto"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="auto",
            name="auto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fset.sale"
            ),
        ),
    ]