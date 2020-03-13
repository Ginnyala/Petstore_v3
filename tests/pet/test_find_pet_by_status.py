from unittest import TestCase
import requests
import json
from tests import BASE_URL
from random import randint


class TestFindPetByStatus(TestCase):
    request_url = f'{BASE_URL}/pet/findByStatus'
    create_url = f'{BASE_URL}/pet'
    header = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    pet = {
        "id": randint(0, 100),
        "category": {
            "id": randint(0, 100),
            "name": "pet_name"
        },
        "name": "puppy",
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

    def test_find_pet_by_status(self):
        response = requests.post(self.create_url, data=json.dumps(self.pet), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

        response = requests.get(self.request_url, params={"status": "available"}, headers=self.header)
        data = response.json()
        found = False
        for pet in data:
            if pet['id'] == self.pet['id']:
                found = True
                assert pet['name'] == self.pet['name'], pet['name']
        assert found == True, 'Pet not found'

    def test_find_pet_by_status_pending(self):
        response = requests.post(self.create_url, data=json.dumps(self.pet), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

        response = requests.get(self.request_url, params={"status": "pending"}, headers=self.header)
        data = response.json()
        assert len(data) > 0

    def test_find_order_bad_id(self):
        response = requests.get(self.request_url, params={"status": "bad_status"}, headers=self.header)
        assert response.status_code == 400, f"Response status code: {response.status_code}"

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.request_url}/{cls.pet['id']}", headers={
            "api_key": 'special-key',
            "accept": "*/*"
        })
