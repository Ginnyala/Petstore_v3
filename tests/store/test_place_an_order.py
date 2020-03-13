from unittest import TestCase
import requests
import json
from random import randint
from tests import BASE_URL


class TestPlaceAnOrder(TestCase):
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

    def test_place_an_order(self):
        response = requests.post(self.request_url, data=json.dumps(self.store), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

        credentials = {
            "id": self.store['id'],
        }
        response = requests.post(self.request_url, data=json.dumps(credentials), headers=self.header)
        data = response.json()
        assert response.status_code == 200, f"Response status code: {response.status_code}"
        assert data['id'] == self.store['id'], f"Response pet id: {data['id']}"

    def test_place_an_invalid_order(self):
        credentials = {
            "id": 'bad id',
        }
        response = requests.post(self.request_url, data=json.dumps(credentials), headers=self.header)
        assert response.status_code == 400
