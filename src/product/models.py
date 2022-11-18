from django.db import models


class ProductType(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        related_name='products',
        null=True,
        blank=True,
    )
    release_date = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
