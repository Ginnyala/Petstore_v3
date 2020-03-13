from unittest import TestCase
import requests
import json
import uuid
from tests import BASE_URL
from random import randint


class TestUpdateUser(TestCase):
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

    def test_update_user(self):
        response = requests.post(self.request_url, data=json.dumps(self.user), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"

        response = requests.delete(
            f"{self.request_url}/{self.user['username']}",
            headers=self.header
        )
        assert response.status_code == 200, f"Response status code: {response.status_code}"

    #def test_update_user_bad_login(self):
    #    credentials = {
    #       "username": 'bad login',
    #    }
    #    response = requests.put(self.request_url, data=json.dumps(credentials), headers=self.header)
    #    assert response.status_code == 400, f"Response status code: {response.status_code}"

    def test_update_user_not_found(self):
        credentials = {
            "username": 'test_user_0',
        }
        response = requests.put(self.request_url, data=json.dumps(credentials), headers=self.header)
        assert response.status_code == 404, f"Response status code: {response.status_code}"

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.request_url}/{cls.user['username']}", headers=cls.header)
