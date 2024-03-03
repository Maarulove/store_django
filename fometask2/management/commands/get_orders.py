from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from fometask2.models import Orders, Goods, Client
from random import choice
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = "get the orders by time"

    def handle(self, *args: Any, **options: Any) -> str | None:
        days = 7
        last_n_days = timezone.now() - timedelta(days=days)

        recent_orders = Orders.objects.filter(date__gte=last_n_days)
        orders = recent_orders.order_by("date")
        
        for order in orders:
            ac = (i.name for i in order.goods.all())
            print(*ac)
        self.stdout.write(f'orders: {orders}')