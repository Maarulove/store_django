from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client, Goods, Orders
from django.utils import timezone
from datetime import timedelta
from .forms import ProductForm
from django.contrib import messages


def init(request):
    return render(request, 'fometask2/index.html')


def sorted_orders(request, client_id, days):
    try:
        client_id = request.GET.get('client_id')
        days = int(request.GET.get('days'))

        Client.objects.get(pk=client_id)
        clients = Client.objects.all()
        client = Client.objects.get(pk=client_id)
        last_n_days = timezone.now() - timedelta(days=days)
        recent_orders = Goods.objects.filter(orders__date__gte=last_n_days, orders__client=client).distinct()
        orders = recent_orders.order_by("date_add")
        
        return render(request, "fometask2/get_orders.html", {"orders": orders, "client":client, "time":days, "clients": clients})

    except:
        messages.success(request, 'Provide a valid id or timeframe!')
        return render(request, 'fometask2/index.html')

def add_goods(request):
    if request.method == "POST": 
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The new product added!')
            return render(request, 'fometask2/index.html')
        
    else:   
        form = ProductForm()
    return render(request, 'fometask2/add_product.html', {'form':form})
