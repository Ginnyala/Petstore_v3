from unittest import TestCase
import requests
import json
from tests import BASE_URL
from random import randint


class TestDeleteOrder(TestCase):
    api_key = 'special-key'
    request_url = f'{BASE_URL}/store/order'
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

    def test_delete_order(self):
        response = requests.post(self.request_url, data=json.dumps(self.store), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

        response = requests.delete(
            f"{self.request_url}/{self.store['id']}",
            headers=self.header
        )
        assert response.status_code == 200, f"Response status code: {response.status_code}"

    def test_delete_order_not_found(self):
        response = requests.delete(f"{self.request_url}/!", headers=self.header)
        assert response.status_code == 404, f"Response status code: {response.status_code}"

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.request_url}/{cls.store['id']}", headers=cls.header)
