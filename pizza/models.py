from django.db import models

# Create your models here.


class Pizza(models.Model):
    PIZZA_SIZES = (
        ('Small', '30 cm'),
        ('Large', '50 cm'),
    )
    name = models.CharField(max_length=60)
    size = models.CharField(max_length=5, choices=PIZZA_SIZES)
    price = models.FloatField()

    def __str__(self):
        return self.name + ' ' + str(self.size) + ' ' + str(self.price) + '€'


class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    pizzas = models.ManyToManyField(Pizza)

    def __str__(self):
        return str(self.client) + ' ' + str(self.date)