from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from fometask2.models import Goods
from django.utils import lorem_ipsum
import random


class Command(BaseCommand):
    help = "Create goods"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name")
        parser.add_argument("price")
    
    def handle(self, *args: Any, **options: Any) -> str | None: 
        name = options.get("name")
        price = options.get("price")

        goods = Goods.objects.create(
            name = name,
            description = lorem_ipsum.sentence(),
            price = price,
            amount = random.randint(1, 100),
        )
        goods.save()
        self.stdout.write(f"goods name: {name}")