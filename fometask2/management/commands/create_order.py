from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from fometask2.models import Orders, Goods, Client
from random import choice



class Command(BaseCommand):
    help = "Create an order"

    def add_arguments(self, parser: CommandParser) -> None: 
        parser.add_argument("client_id")
        parser.add_argument("goods_id")

    def handle(self, *args: Any, **options: Any) -> str | None:
        cl = options.get("client_id")
        gd = options.get("goods_id")
        
        clients = Client.objects.all()
        goods_list = Goods.objects.all()

        print(cl)
        client = clients.filter(name=cl).first()
        goods = goods_list.filter(name=gd).first()
        print(goods, 654656)
        
        
        
        order, abc = Orders.objects.get_or_create(total_amount=5001.4)

        order.client.add(client)
        order.goods.add(goods)
        order.save()
        self.stdout.write(f"Order:{order} ")
    