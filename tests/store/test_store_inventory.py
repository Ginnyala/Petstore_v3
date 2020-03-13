from unittest import TestCase
import requests
import json
from tests import BASE_URL
from random import randint


class TestStoreInventory(TestCase):
    request_url = f'{BASE_URL}/store/inventory'
    header = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "api_key": "special-key"
    }
    store = {
        "id": randint(0, 100),
        "petId": 0,
        "quantity": 0,
        "shipDate": "2020-03-10T12:48:47.179Z",
        "status": "placed",
        "complete": True
    }

    def test_store_inventory(self):
        response = requests.get(self.request_url, params={"status": "placed"}, headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"
