from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

    def  __str__(self) -> str:
        return f"Name: {self.name}"
    
class Goods(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    amount = models.IntegerField()
    date_add = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Name: {self.name}"


class Orders(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    goods = models.ManyToManyField(Goods)
    total_amount = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.client}, {self.goods}"
