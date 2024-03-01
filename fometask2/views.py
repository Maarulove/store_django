from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Goods, Orders
from django.utils import timezone
from datetime import timedelta
# Create your views here.


def sorted_orders(request, client_id):

    days = 30
    days = 2
    days = 365

    client = Client.objects.get(pk=client_id)
    last_n_days = timezone.now() - timedelta(days=days)

    # recent_orders = Orders.objects.filter(date__gt=last_n_days, client=client)
    recent_orders = Goods.objects.filter(orders__date__gte=last_n_days, orders__client=client)
    

    # orders = recent_orders.order_by("date")
    print(client)
    orders = recent_orders.order_by("date_add")

    return render(request, "fometask2/get_orders.html", {"orders": orders, "client":client, "time":days})