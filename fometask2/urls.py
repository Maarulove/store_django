from django.urls import path
from . import views

urlpatterns = [
    path("sorted_orders/<int:client_id>", views.sorted_orders, name="sorted_orders"),
    path("add_product", views.add_goods, name="add_product"),

]