from django.urls import path
from . import views

urlpatterns = [
    path("", views.init, name="init"),
    path("sorted_orders/<int:client_id>/<int:days>", views.sorted_orders, name="sorted_orders"),
    path("add_product", views.add_goods, name="add_product"),
    path("goods", views.goods_list, name="goods"),
    path("clients", views.client_list, name="clients"),

]