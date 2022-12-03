from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Sale(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f"Модель: {self.name}"


class Auto(models.Model):
    auto = models.ForeignKey(Sale, on_delete=models.CASCADE)
    auto_name = models.CharField(max_length=50)
    auto_price = models.IntegerField(
        validators=[
            MinValueValidator(1),
        ],
        blank=False,
    )


class Specs(models.Model):
    spec = models.ForeignKey(Auto, on_delete=models.CASCADE)
    spec_name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
