from pprint import pprint
import requests
import datetime

class UseGDrive:
    url = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, token: str):
        self.token = token
    
    # Метод создает необходимые заголовки с токеном для доступа к диску
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }