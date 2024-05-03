from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import Driver, Vehicle, AccountingRegistry

# Register your models here.


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="drivers.csv"'
        writer = csv.writer(response)
        writer.writerow(["RUT", "Name", "Last Name", "Active", "Created At", "Vehicle"])
        for driver in queryset:
            writer.writerow(
                [
                    driver.rut,
                    driver.name,
                    driver.last_name,
                    driver.active,
                    driver.created_at,
                    driver.vehicle,
                ]
            )
        return response

    export_to_csv.short_description = "Export selected drivers to CSV"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="vehicles.csv"'
        writer = csv.writer(response)
        writer.writerow(
            ["Registration Plate", "Brand", "Model", "Year", "Active", "Created At"]
        )
        for vehicle in queryset:
            writer.writerow(
                [
                    vehicle.registration_plate,
                    vehicle.brand,
                    vehicle.model,
                    vehicle.year,
                    vehicle.active,
                    vehicle.created_at,
                ]
            )
        return response

    export_to_csv.short_description = "Export selected vehicles to CSV"


@admin.register(AccountingRegistry)
class AccountingRegistryAdmin(admin.ModelAdmin):
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            'attachment; filename="accountingregistries.csv"'
        )
        writer = csv.writer(response)
        writer.writerow(["Date of Purchase", "Price", "Vehicle"])
        for accounting_registry in queryset:
            writer.writerow(
                [
                    accounting_registry.date_of_purchase,
                    accounting_registry.price,
                    accounting_registry.vehicle,
                ]
            )
        return response

    export_to_csv.short_description = "Export selected accounting registries to CSV"
