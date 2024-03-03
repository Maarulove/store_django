from typing import Any
from django.core.management.base import CommandParser
from fometask2.models import Client
from django.core.management import BaseCommand



class Command(BaseCommand):
    help = "Create Author"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name")

    def handle(self, *args: Any, **options: Any) -> str | None:
        name = options.get("name")

        client = Client.objects.create(
            name=name,
            email=f"{name}@mail.ru",
            phone="790 432 543",
            adress="Adress adress 45",
            date="2000-10-30",
        )
        client.save()
        self.stdout.write(f"{client}")

