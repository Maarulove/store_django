from django.urls import path
from . import views

urlpatterns = [
    path("sorted_orders/<int:client_id>", views.sorted_orders, name="sorted_orders"),
]


