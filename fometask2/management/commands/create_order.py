from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from fometask2.models import Orders, Goods, Client
from random import choice



class Command(BaseCommand):
    help = "Create an order"

    def add_arguments(self, parser: CommandParser) -> None: 
        parser.add_argument("goods_amount", type=int)

    def handle(self, *args: Any, **options: Any) -> str | None:
        goods_amount = options.get('goods_amount')
        clients = Client.objects.all()
        goods_list = Goods.objects.all()

        # client = clients.filter(name=cl).first()
        # # goods = goods_list.filter(name__in=gd)

        # goods = Goods.objects.filter(name__in=gd)
        
        order = Orders.objects.create(
            client = choice(clients),
            total_amount = 0,
        )

    

        # print(goods)
        for i in range(goods_amount):
            gd_ls = choice(goods_list)
            order.goods.add(gd_ls)
            order.total_amount += gd_ls.price 

        order.save()
        print(order.goods)
        # print(goods)
        # print(order.goods)
        self.stdout.write(f"Order: Client {order} ")
    