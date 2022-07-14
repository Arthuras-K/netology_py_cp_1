import requests
from pprint import pprint
from tqdm import tqdm 
import time


class UseVK:
    url = 'http://api.vk.com/method/'

    def __init__(self, VER_API_VK: str, TOKEN_VK_PH: str):
        self.params = {
            'access_token': TOKEN_VK_PH,
            'v': VER_API_VK
        }

    # Метод возвращает словарь "count" фото
    def get_photos(self, id_user = None, count = None, album_id = "profile") -> list:
        method_params = {
            "owner_id": id_user,
            "count": count,
            "album_id": album_id,
            "rev": 1,
            "extended": 1,
            "photo_sizes": 1
        }
        method_url = self.url+"photos.get"
        response = requests.get(method_url, params={**self.params,**method_params})
        if 'error' in response.json():
            return print(f' - Ошибка! Страница id={id_user} удалена или нет доступа')                  
        if response.status_code == 200:
            print(' - Запрос к "api.vk" выполнен успешно')
        else:
            return print(' - Ошибка запроса к "api.vk"! Код:', response.status_code)
        if response.json()['response']['count'] == 0:
            return print(f" - Ошибка! У профиля id={id_user} нету фотографий")
        count_photos = []
        for photo in tqdm(response.json()['response']['items'], desc=' - Получение фотографий'):
            count_photos.append({
                'likes':photo['likes']['count'], 
                'url':photo['sizes'][-1]['url']
                })
            time.sleep(0.05)
        return count_photos

    # Метод сортирует фото по количеству лайков и убиарет лишние
    def sorted_photos(self, photos_dict, qty_photos = 5) -> list:
        sorted_list = sorted(photos_dict, key=lambda x: x['likes'], reverse=True)[:qty_photos]
        print(f' - Фотографии отсортированы\n - Получен список из топ-{qty_photos}')
        # Цикл для проверки уникальности количества лайков, при повторе добавление '*'
        for el in sorted_list:
            likes = str(el['likes'])
            while True:
                if likes not in [i['likes'] for i in sorted_list]:
                    el['likes'] = likes
                    break
                likes += '*'
        return sorted_list