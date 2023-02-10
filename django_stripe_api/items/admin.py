from django.contrib import admin

from items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Class to customize Items display in admin panel."""

    list_display = ["pk", "name", "description", "price"]
    search_fields = ["name"]
