from django.urls import path

from . import views

app_name = "items"

urlpatterns = [
    path("buy/<int:id>/", views.buy, name="buy"),
    path("item/<int:id>/", views.item, name="item"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
]
