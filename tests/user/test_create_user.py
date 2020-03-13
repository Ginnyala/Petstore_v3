from unittest import TestCase
import requests
import json
from random import randint
from tests import BASE_URL


class TestCreateUser(TestCase):
    request_url = f'{BASE_URL}/user'
    header = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    user = {
        "id": randint(0, 100),
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 1
    }

    def test_create_user(self):
        response = requests.post(self.request_url, data=json.dumps(self.user), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

    def test_user_exists(self):
        response = requests.get(f"{self.request_url}/{self.user['username']}", headers={"accept": "application/json"})
        assert response.status_code == 200, f"Response status code: {response.status_code}"

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.request_url}/{cls.user['username']}", headers=cls.header)
