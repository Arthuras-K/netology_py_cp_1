from pprint import pprint
import yaml
import class_vk as vk
import class_yd as yd


if __name__ == '__main__':
    print('  \u2665   \u2665   \u2665   \u2665   \u2665\
        \nДобро пожаловать в программу поиска и сохранения\
        \nна диск топ-5 фото пользователя ВК по лайкам.\
        \n  \u2665   \u2665   \u2665   \u2665   \u2665')

    limit_photos = 500 # Максимальное количество (выборка) для сортировки по лайкам    
    return_photos = 5 #  Итоговое кол-во для сохранения на диск
    album = 'profile' # 'profile' — фотографии брать из профиля, 'wall' — фотографии со стены
    target_disk = 'yandex' # 'yandex' — фотографии сохранять на yandexdisk, 'google' — фотографии сохранять на googledisk

    with open('config.yaml') as f:
        config = yaml.safe_load(f)
        token_vk_ph = config['token_vk_ph'] # Токен от ВК с доступом к фото
        version_api_vk = config['version_api'] # Версия АПИ ВК
        token_yd = config['token_yd'] # Токен от ЯД для сохранения фото

    while True:
        # id_vk = input("Введите id страницы: ")
        id_vk = '103457'
        if id_vk.isnumeric() and int(id_vk) > 0:
            break
        print('Некорректное значение')
    
    use_vk = vk.UseVK(version_api_vk, token_vk_ph)
    photos_list = use_vk.get_photos(id_vk, limit_photos, album)  
    photos_top = use_vk.sorted_photos(photos_list, return_photos)
        
    use_yd = yd.UseYDisk(token_yd)
    use_yd.upload_file_to_disk(path_to_yd, photos_top, id_vk)
