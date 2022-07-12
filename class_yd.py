from pprint import pprint
import requests
import datetime

class UseYDisk:
    url = 'https://cloud-api.yandex.net/v1/disk/'
    path_to_folder = 'TOP-PHOTOS'    

    def __init__(self, token: str):
        self.token = token
    
    # Метод создает необходимые заголовки с токеном для доступа к диску
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # Метод создает необходимые папки (путь)
    def create_folder(self, id_user = 'Self', qty_photos = 5) -> str:
        files_url = self.url + 'resources/'
        headers = self.get_headers()
        params = {'path':'disk:/top-VK'}
        response = requests.put(files_url, headers=headers, params=params)
        path_to = 'disk:/top-VK/' + 'id=' + str(id_user) + ' TOP-' + str(qty_photos) + ' photos'
        params = {'path': path_to}
        response = requests.put(files_url, headers=headers, params=params)       
        if response.status_code == 201:
            print(" - Создан путь на диске")
            return path_to
        elif response.status_code == 409:
            path_to += ' (' + str(datetime.datetime.today() + datetime.timedelta())[:-5] + ')'
            params = {'path': path_to}
            response = requests.put(files_url, headers=headers, params=params)  
            if response.status_code == 201:
                print(" - Создан путь на диске")
                return path_to
            else:
                print(' - Ошибка! Код:', response.status_code)  
        else:
            print(' - Ошибка! Код:', response.status_code)       


    # Метод загружает файл по сылке на диск
    def upload_file_to_disk(self, disk_file_path, photos_list):
        upload_url = self.url + 'resources/upload'
        count = 0
        for el in photos_list:
            count += 1
            params = {'path': disk_file_path + '/' + str(count) + ' likes-' + el['likes'] + '.jpg', 'url': el['url']} 
            headers = self.get_headers()
            response = requests.post(upload_url, params=params, headers=headers)
            if response.status_code == 202:
                print(f' - Файл {count} успешно загружен')
            else:
                print(' - Ошибка! Код:', response.status_code)
        print(' - Конец загрузки на Яндекс.Диск\n')           


