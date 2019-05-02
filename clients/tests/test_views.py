from django.test import TestCase, Client
from django.urls import reverse
import json


from ..models import Client as PClient

class TestViews(TestCase):

    def test_client_list_GET(self):
        client = Client()

        response = client.get('clients:client-list')

        #self.assertEqual(response.status_code, 200)
        print(json.loads(response.content)['data'])
        #self.assertEqual(json.loads(response.content)['data'], [])
        #self.assertTemplateUsed(response, 'clients/client_list.html')