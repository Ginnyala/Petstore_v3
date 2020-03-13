from unittest import TestCase
import requests
import json
from random import randint
from tests import BASE_URL


class TestFindOrderID(TestCase):
    request_url = f'{BASE_URL}/store/order'
    header = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "api_key": "special-key",
    }
    store = {
        "id": randint(0, 100),
        "petId": 0,
        "quantity": 0,
        "shipDate": "2020-03-10T12:56:20.228Z",
         "status": "placed",
        "complete": True
    }

    def test_find_order(self):
        response = requests.post(self.request_url, data=json.dumps(self.store), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

        response = requests.get(
            f"{self.request_url}/{self.store['id']}",
            headers=self.header
        )
        data = response.json()
        assert response.status_code == 200, f"Response status code: {response.status_code}"
        assert data['id'] == self.store['id'], f"Response pet id: {data['id']}"

    def test_find_order_bad_id(self):
        response = requests.get(f"{self.request_url}/test id", headers=self.header)
        assert response.status_code == 400, f"Response status code: {response.status_code}"

    def test_find_order_not_found(self):
        response = requests.get(f"{self.request_url}/test_id_0", headers=self.header)
        assert response.status_code == 404, f"Response status code: {response.status_code}"

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.request_url}/{cls.store['id']}", headers=cls.header)
