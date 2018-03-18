from django.test import TestCase
from django.test.client import Client


class TestRest(TestCase):
    def test_users(self):
        c = Client()
        resp = c.get('/users/')
        print(resp.content)
