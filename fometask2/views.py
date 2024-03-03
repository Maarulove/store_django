from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client, Goods, Orders
from django.utils import timezone
from datetime import timedelta
from .forms import ProductForm
# Create your views here.


def sorted_orders(request, client_id):

    days = 30
    days = 2
    days = 365

    client = Client.objects.get(pk=client_id)
    last_n_days = timezone.now() - timedelta(days=days)

    recent_orders = Goods.objects.filter(orders__date__gte=last_n_days, orders__client=client)
    orders = recent_orders.order_by("date_add")

    return render(request, "fometask2/get_orders.html", {"orders": orders, "client":client, "time":days})


def add_goods(request):
    if request.method == "POST": 
        form = ProductForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, 'fometask2/image.html', {'form': form})
        
    else:   
        form = ProductForm()
    return render(request, 'fometask2/add_product.html', {'form':form})
