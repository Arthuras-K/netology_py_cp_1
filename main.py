import yaml
from pprint import pprint
import class_vk as vk
import class_yd as yd


if __name__ == '__main__':
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
        token_vk_ph = config['token_vk_ph']
        version_api = config['version_api']

qty_photos = 5
id_vk = 1
target_disk = 'yandex'

result = vk.UseVK(version_api, token_vk_ph)
pprint(result.get_photos_list(id_user=1, count=2))
print(777777777777777,len(result.get_photos_list(id_user=1)['response']["items"]))


