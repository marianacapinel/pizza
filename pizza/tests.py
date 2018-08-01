from rest_framework import status
from rest_framework.test import APITestCase
from .models import Pizza, Client


class OrderTests(APITestCase):

       def test_create_order(self):
                url = 'http://127.0.0.1:8000/orders/'
                Pizza.objects.create(name="Salami", size="Small", price=2)
                Client.objects.create(name="Test", address="Berlin")
                data = {"date": "2018-07-25", "client": 1, "pizzas": [1]}
                response = self.client.post(url, data, format='json')
                print(response.content)
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
