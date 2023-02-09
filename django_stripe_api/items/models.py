from django.db import models


class Item(models.Model):
    """Class to store items in the database."""

    name = models.CharField("Item name", max_length=200, unique=True)  # uniq?
    description = models.TextField("Item description")
    price = models.FloatField("Item price")
