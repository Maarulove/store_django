from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from fometask2.models import Orders, Goods, Client
from random import choice



class Command(BaseCommand):
    help = "Create an order"

    def add_arguments(self, parser: CommandParser) -> None: 
        parser.add_argument("client_name")
        parser.add_argument("goods_name")

    def handle(self, *args: Any, **options: Any) -> str | None:
        cl = options.get("client_name")
        gd = options.get("goods_name")
        
        clients = Client.objects.all()
        goods_list = Goods.objects.all()

        client = clients.filter(name=cl).first()
        goods = goods_list.filter(name=gd).first()
        
        
        
        order, abc = Orders.objects.get_or_create(total_amount=5001.4)

        order.client.add(client)
        order.goods.add(goods)
        order.save()
        self.stdout.write(f"Order:{order} ")
    