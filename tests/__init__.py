import os


PETSTORE_URL = 'https://petstore3.swagger.io/api/v3'
BASE_URL = os.getenv('BASE_URL', PETSTORE_URL)
