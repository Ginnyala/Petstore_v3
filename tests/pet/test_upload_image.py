from unittest import TestCase
import json
from tests import BASE_URL
from random import randint
import requests
import os


class TestUploadImage(TestCase):
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

    def test_update_pet(self):
        response = requests.post(self.request_url, data=json.dumps(self.pet), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

        file = open(os.path.join(os.path.dirname(__file__), './assets/pet.png'), 'rb')
        files = {'media': file}
        response = requests.post(
            f"{self.request_url}/{self.pet['id']}/uploadImage",
            headers={
                "accept": "application/json",
                "Content-Type": "application/octet-stream",
            },
            files=files
        )
        file.close()
        data = response.json()

        assert response.status_code == 200, f"Response status code: {response.status_code}"
        assert data['id'] == self.pet['id'], f"Response pet id: {data['id']}"

    @classmethod
    def tearDownClass(cls):
        requests.delete(cls.request_url, data=json.dumps(cls.pet['id']), headers=cls.header)
