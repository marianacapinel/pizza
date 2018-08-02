from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase

from pizza.models import Pizza, Client, Order


class OrderTests(APITestCase):
    def test_create_order(self):
        pizza = Pizza.objects.create(name='Salami', size='Small', price=2)
        client = Client.objects.create(name='Test', address='Berlin')
        data = {
            'date': '2018-07-25',
            'client': client.id,
            'pizzas': [pizza.id]
        }

        response = self.client.post('/orders/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # verifying that order was saved in the database and contains
        # data from the request
        order_id = response.json()['id']
        order = Order.objects.get(id=order_id)
        self.assertEqual(order.client, client)
        self.assertEqual(list(order.pizzas.all()), [pizza])
        self.assertEqual(order.date, date(2018, 7, 25))
