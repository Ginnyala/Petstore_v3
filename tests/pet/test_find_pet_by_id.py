from unittest import TestCase
import requests
import json
from tests import BASE_URL
from random import randint


class TestFindPetById(TestCase):
    api_key = 'special-key'
    request_url = f'{BASE_URL}/pet'
    header = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "api_key": "special-key"
    }
    pet = {
        "id": randint(0, 100),
        "category": {
            "id": randint(0, 100),
            "name": "pet_name"
        },
        "name": "doggie",
        "photoUrls": [
            "data:image/jpeg;base64,/9j/4AAQSkZJRgA"
        ],
        "tags": [
            {
                "id": randint(0, 100),
                "name": "pet_name"
            }
        ],
        "status": "available"
    }

    def test_find_pet_by_id(self):
        response = requests.post(self.request_url, data=json.dumps(self.pet), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

        response = requests.get(
            f"{self.request_url}/{self.pet['id']}",
            headers=self.header
        )
        data = response.json()
        assert response.status_code == 200, f"Response status code: {response.status_code}"
        assert data['id'] == self.pet['id'], f"Response pet id: {data['id']}"
        assert data['name'] == self.pet['name'], f"Response pet id: {data['name']}"

    def test_find_order_bad_id(self):
        response = requests.get(f"{self.request_url}/test id", headers=self.header)
        assert response.status_code == 400, f"Response status code: {response.status_code}"

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.request_url}/{cls.pet['id']}", headers=cls.header)
