import requests
# import progress
# import tqdm
from pprint import pprint


class UseVK:
    url = 'http://api.vk.com/method/'

    def __init__(self, version_api: str, token: str):
        self.params = {
            'access_token': token,
            'v': version_api
        }
    

    # Метод возвращает список фото
    def get_photos_list(self, id_user = None, album_id = "profile", count = None):
        # album_id : wall, profile, saved 
        photos_list_params = {
            "owner_id": id_user,
            "album_id": album_id,
            "rev": 1,
            "extended": 1,
            "photo_sizes": 1,
            "count": count
        }
        photos_list_url = self.url+"photos.get"
        response = requests.get(photos_list_url, params={**self.params,**photos_list_params})
        return response.json()

    # Метод получает ссылку и место необходимые для загрузки на диск
    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        # Параметр "overwrite" - перезапись файла если он там уже есть
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        if response.status_code == 200:
            print("Cсылка получена")
        else:
            print('Ошибка! Код:', response.status_code)
        return response.json()

    # Метод загружает файл через полученную ссылку
    def upload_file_to_disk(self, disk_file_path, filename):
        # Под ключом "href" находится неободимая ссылка, поэтому методом get для словаря достает значение
        href = self.get_upload_link(disk_file_path=disk_file_path).get("href", "")
        # Запрос на сохранение файла по полученной ссылке 
        response = requests.put(href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print(f"Файл '{filename}' успешно загружен")
        else:
            print('Ошибка! Код:', response.status_code)
