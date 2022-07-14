from pprint import pprint
import yaml
import class_vk as vk
import class_yd as yd
import class_gd as gd


if __name__ == '__main__':
    print('\n  \u2665       \u2665       \u2665       \u2665      \u2665\
        \n    Добро пожаловать в программу\
        \n   сортировки и сохранения на диск\
        \nтоп-5 фото пользователя ВК по лайкам.\
        \n  \u2665       \u2665       \u2665       \u2665      \u2665\n')

    while True:
        limit_photos = 500 # Максимальное количество (выборка) для сортировки по лайкам    
        return_photos = 5 #  Итоговое кол-во для сохранения на диск
        album = 'profile' # 'profile' — фотографии брать из профиля, 'wall' — фотографии со стены
        target_disk = 'yandex' # 'yandex' — фотографии сохранять на yandexdisk, 'google' — фотографии сохранять на googledrive
        
        
        with open('config.yaml') as f:
            config = yaml.safe_load(f)
            TOKEN_VK_PH = config['token_vk_ph'] # Токен от ВК с доступом к фото
            VER_API_VK = config['version_api'] # Версия АПИ ВК
            TOKEN_YD = config['token_yd'] # Токен от Яндекс.Диск
            TOKEN_GD = config['token_gd'] # Токен от Google Диск

        while True:
            id_vk = input("Введите id страницы: ")
            if id_vk == '':
                id_vk = None
                break
            elif id_vk.isnumeric() and int(id_vk) > 0:
                break
            print(' - Некорректное значение')
        
        name_folder = f'disk:/top-VK/Id={str(id_vk)} TOP-{str(return_photos)} photos' # Имя папки и файла для сохранения на диск     

        use_vk = vk.UseVK(VER_API_VK, TOKEN_VK_PH)
        photos_list = use_vk.get_photos(id_vk, limit_photos, album)
        if not isinstance(photos_list, list):
            continue        
        photos_top = use_vk.sorted_photos(photos_list, return_photos)

        if  'yandex' in target_disk:
            use_yd = yd.UseYDisk(TOKEN_YD)
            disk_file_path = use_yd.create_folder(name_folder)
            count = 0
            for data in photos_top:
                count += 1
                photo_name = f"{disk_file_path}/{str(count)} likes-{data['likes']}.jpg"
                photo_url = data['url']
                use_yd.upload_file_to_disk(photo_name, photo_url)  
            print(' - Конец загрузки на Яндекс.Диск\n')   

        if  'google' in target_disk: 
            use_gd = gd.UseGDrive(TOKEN_GD)

      