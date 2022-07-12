import requests
import time
from tqdm import tqdm 


class UseYDisk:

    path_to_yd = 'netology/top-'    

    def __init__(self, token: str):
        self.token = token
    
    # Метод создает необходимые заголовки с токеном для доступа к диску
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # Метод возвращает словарь с перечнем файлов на диске, просто для теста
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        params = {'offset': 1, 'limit': 3}
        response = requests.get(files_url, headers=headers, params=params)
        return response.json()

    # Метод загружает файл по сылке на диск
    def upload_file_to_disk(self, disk_file_path, photos_dict):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        count = 0
        for url_photo, likes in photos_dict.items():
            count += 1
            params = {'path': disk_file_path + str(count) + '_likes-' + likes + '.jpg', 'url': url_photo} 
            headers = self.get_headers()
            response = requests.post(upload_url, params=params, headers=headers)
            if response.status_code == 202:
                print(f"Файл успешно загружен")
            else:
                print('Ошибка! Код:', response.status_code)


