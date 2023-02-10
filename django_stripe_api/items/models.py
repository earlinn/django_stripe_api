from django.db import models


class Item(models.Model):
    """Class to store items in the database."""

    name = models.CharField("Item name", max_length=200, unique=True)  # uniq?
    description = models.TextField("Item description", null=True, blank=True)
    price = models.PositiveIntegerField("Item price")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name
