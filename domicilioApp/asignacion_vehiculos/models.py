from django.db import models
from django.db.models import PROTECT
from django.utils import timezone


# Create your models here.
class Driver(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    vehicle = models.OneToOneField(
        "Vehicle",
        related_name="driver",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.rut

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
        ordering = ["rut"]


class Vehicle(models.Model):
    registration_plate = models.CharField(max_length=6, primary_key=True)
    brand = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=False, blank=False)
    year = models.DateField(null=False, blank=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.registration_plate

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
        ordering = ["registration_plate"]


class AccountingRegistry(models.Model):
    date_of_purchase = models.DateField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    vehicle = models.OneToOneField(
        "Vehicle", related_name="contabilidad", on_delete=PROTECT
    )

    def __str__(self):
        return self.vehicle.registration_plate

    class Meta:
        verbose_name = "Accounting Registry"
        verbose_name_plural = "Accounting Registries"
        ordering = ["date_of_purchase"]
