from django.db import models
from django.contrib.auth import get_user_model


class Company(models.Model):

    class Meta:
        verbose_name_plural = 'companies'

    class CompanyType(models.IntegerChoices):
        FACTORY = 0
        DISTRIBUTOR = 1
        DEALERSHIP = 2
        RETAIL_NETWORK = 3
        SOLE_TRADER = 4
    type = models.SmallIntegerField(
        choices=CompanyType.choices,
    )
    name = models.CharField(
        unique=True,
        max_length=100,
    )
    email = models.EmailField(
        unique=True,
        max_length=100,
        null=True,
        blank=True,
    )
    country = models.ForeignKey(
        'reference.Country',
        related_name='companies',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        'reference.City',
        related_name='companies',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    street = models.CharField(
        max_length=100
    )
    house_number = models.CharField(
        max_length=10
    )
    products = models.ManyToManyField(
        'product.Product',
        related_name='companies',
    )
    employees = models.ManyToManyField(
        get_user_model(),
        related_name='companies',
    )
    shipper = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    debt = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
