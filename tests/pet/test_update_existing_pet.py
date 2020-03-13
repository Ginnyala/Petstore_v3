from unittest import TestCase
import requests
import json
from tests import BASE_URL
from random import randint


class TestUpdateExistingPet(TestCase):
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

    def test_update_existing_pet(self):
        response = requests.post(self.request_url, data=json.dumps(self.pet), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

    def test_update_user_bad_login(self):
        credentials = {
            "id": 'bad id',
        }
        response = requests.put(self.request_url, data=json.dumps(credentials), headers=self.header)
        assert response.status_code == 400, f"Response status code: {response.status_code}"

    def test_update_existing_pet_not_found(self):
        credentials = {
            "id": 'test_id_0',
        }
        response = requests.put(self.request_url, data=json.dumps(credentials), headers=self.header)
        assert response.status_code == 404, f"Response status code: {response.status_code}"

    def test_update_existing_pet_validation_exception(self):
        response = requests.put(self.request_url, data=json.dumps(self.pet), headers=self.header)
        assert response.status_code == 405, f"Response status code: {response.status_code}"

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.request_url}/{cls.pet['id']}", headers=cls.header)
