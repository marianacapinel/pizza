from rest_framework import serializers
from .models import Order, Client, Pizza


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = '__all__'
