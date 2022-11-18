from django.db import models


class Country(models.Model):

    class Meta:
        verbose_name_plural = 'countries'

    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name


class City(models.Model):

    class Meta:
        verbose_name_plural = 'cities'

    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        related_name='cities',
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
