from django.contrib import admin
import nested_admin

from .models import Sale, Auto, Specs


class SpecsAdmin(nested_admin.NestedStackedInline):
    model = Specs


class AutoAdmin(nested_admin.NestedStackedInline):
    model = Auto
    inlines = [SpecsAdmin]


class SalesAdmin(nested_admin.NestedModelAdmin):
    inlines = [AutoAdmin]


admin.site.register(Sale, SalesAdmin)
