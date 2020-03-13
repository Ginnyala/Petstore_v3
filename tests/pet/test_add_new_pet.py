from unittest import TestCase
import requests
import json
from random import randint
from tests import BASE_URL


class TestAddNewPet(TestCase):
    api_key = 'special-key'
    request_url = f'{BASE_URL}/pet'
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

    def test_add_new_pet(self):
        response = requests.post(self.request_url, data=json.dumps(self.pet), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.request_url}/{cls.pet['id']}", headers=cls.header)
