from pprint import pprint
import requests
import datetime

class UseYDisk:
    url = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, TOKEN_YD: str):
        self.token = TOKEN_YD
    
    # Метод создает необходимые заголовки с токеном для доступа к диску
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # Метод создает необходимые папки (путь), если папка с заданным именем еуже есть, то создает рядом еще одну добавив к имени дату
    def create_folder(self, path_to) -> str:
        files_url = self.url + 'resources/'
        headers = self.get_headers()
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
                print(" - Создан путь на диске для загрузки")
                return path_to
            else:
                print(' - Ошибка! Код:', response.status_code)  
        else:
            print(' - Ошибка! Код:', response.status_code)       


    # Метод загружает файл по сылке на диск
    def upload_file_to_disk(self, file_name, file_url):
        upload_url = self.url + 'resources/upload'
        params = {'path': file_name, 'url': file_url} 
        headers = self.get_headers()
        response = requests.post(upload_url, params=params, headers=headers)
        if response.status_code == 202:
            print(f' - Файл {file_name.split("/")[-1]} успешно загружен')
        else:
            print(' - Ошибка! Код:', response.status_code)

