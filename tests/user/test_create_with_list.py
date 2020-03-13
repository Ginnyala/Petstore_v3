from unittest import TestCase
import requests
import json
from random import randint
from tests import BASE_URL


class TestCreateUserWithList(TestCase):
    request_url = f'{BASE_URL}/user/createWithList'
    header = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    users = [
        {
            "id": randint(0, 100),
            "username": "test_user_1",
            "firstName": "test_first_name_1",
            "lastName": "test_last_name_1",
            "email": "test_user_1@example.com",
            "password": "test_pass_1",
            "phone": "+48111333444",
            "userStatus": 0
        },
        {
            "id": randint(0, 100),
            "username": "test_user_2",
            "firstName": "test_first_name_2",
            "lastName": "test_last_name_2",
            "email": "test_user_2@example.com",
            "password": "test_pass_2",
            "phone": "+48111333442",
            "userStatus": 0
        }
    ]

    def test_create_user_with_list(self):
        response = requests.post(self.request_url, data=json.dumps(self.users), headers=self.header)
        assert response.status_code == 200, f"Response status code: {response.status_code}"
