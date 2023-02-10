import os

import stripe
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, redirect, render

from .models import Item
from django_stripe_api.settings import MODE

stripe.api_key = os.getenv("STRIPE_TEST_KEY")


def buy(request, id):
    """Gets a Stripe Session Id to pay for the selected item."""
    item = get_object_or_404(Item, pk=id)
    if MODE == "dev":
        domain = get_current_site(request)
    else:
        domain = "localhost"
    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                        "description": item.description,
                    },
                    "unit_amount": item.price,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=f"http://{domain}/success",
        cancel_url=f"http://{domain}/cancel",
    )
    return redirect(session.url)


def item(request, id):
    """Shows info on a particular item and a buy button."""
    item = get_object_or_404(Item, pk=id)
    return render(request, "item.html", {"item": item})


def success(request):
    """Shows a success page."""
    return render(request, "success.html")


def cancel(request):
    """Shows a cancel page."""
    return render(request, "cancel.html")


# add custom errors pages
