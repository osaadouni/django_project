from django.test import TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer

from ..views import ClientList, ClientDetail, ClientCreate, ClientUpdate, ClientDelete, ClientSearchForm
from ..models import Client


class TestUrls(TestCase):

    def test_list_url_resolves(self):
        url = reverse('clients:client-list')
        self.assertEqual(resolve(url).func.view_class, ClientList)


    def test_add_url_resolves(self):
        url = reverse('clients:client-add')
        self.assertEqual(resolve(url).func.view_class, ClientCreate)


    def test_detail_url_resolves(self):
        client = mixer.blend(Client)
        url = reverse('clients:client-detail', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, ClientDetail)

    def test_update_url_resolves(self):
        client = mixer.blend(Client)
        url = reverse('clients:client-edit', args=[1])
        self.assertEqual(resolve(url).func.view_class, ClientUpdate)

    def test_delete_url_resolves(self):
        client = mixer.blend(Client)
        url = reverse('clients:client-delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, ClientDelete)
