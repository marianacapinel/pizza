from rest_framework import generics
from . import models
from . import serializers
from .models import Order

# Create your views here.


class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class RetrieveUpdateDestroyOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class ListOrderClient(generics.ListAPIView):
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        client = self.kwargs['client']
        return Order.objects.filter(client=client)


class ClientList(generics.ListAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class ClientDetailstList(generics.RetrieveAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class PizzaList(generics.ListAPIView):
    queryset = models.Pizza.objects.all()
    serializer_class = serializers.PizzaSerializer



class PizzaDetailstList(generics.RetrieveAPIView):
    queryset = models.Pizza.objects.all()
    serializer_class = serializers.PizzaSerializer