from unittest import TestCase
import requests
import json
from random import randint
from tests import BASE_URL


class TestDeleteUser(TestCase):
    login_url = f'{BASE_URL}/user/login'
    request_url = f'{BASE_URL}/user'
    header = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "api_key": "special-key"
    }
    user = {
        "id": randint(0, 100),
        "username": "test_user",
        "firstName": "test_first_name",
        "lastName": "test_last_name",
        "email": "test_user@example.com",
        "password": "test_pass",
        "phone": "+48111333444",
        "userStatus": 0
    }

    def test_delete_user(self):
        response = requests.post(self.request_url, data=json.dumps(self.user), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

        response = requests.delete(
            f"{self.request_url}/{self.user['username']}",
            headers=self.header
        )
        assert response.status_code == 200, f"Response status code: {response.status_code}"

    def test_delete_user_not_found(self):
        response = requests.delete(f"{self.request_url}/!", headers=self.header)
        assert response.status_code == 404, f"Response status code: {response.status_code}"

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.request_url}/{cls.user['username']}", headers=cls.header)
