from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase

from pizza.models import Pizza, Client, Order


class OrderTests(APITestCase):
    def setUp(self):
        # some fixtures that we can use in every test
        self.pizza = Pizza.objects.create(name='Salami', size='Small', price=2)
        self.customer = Client.objects.create(name='Test', address='Berlin')

    def test_create_order(self):
        data = {
            'date': '2018-07-25',
            'client': self.customer.id,
            'pizzas': [self.pizza.id]
        }

        response = self.client.post('/orders/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # verifying that order was saved in the database and contains
        # data from the request
        order_id = response.json()['id']
        order = Order.objects.get(id=order_id)
        self.assertEqual(order.client, self.customer)
        self.assertEqual(list(order.pizzas.all()), [self.pizza])
        self.assertEqual(order.date, date(2018, 7, 25))

    def test_delete_order(self):
        order = Order.objects.create(client=self.customer, date=date(2018, 7, 25))
        order.pizzas.set([self.pizza])

        response = self.client.delete('/orders/{}/'.format(order.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(Order.objects.filter(id=order.id).first())
