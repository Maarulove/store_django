from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Goods, Orders
# Create your views here.


def create_client(request):
    help = "create new client"

