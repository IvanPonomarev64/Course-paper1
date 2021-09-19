import requests
import os
import json
import time
from progress.bar import Bar
from pprint import pprint

id = '552934290'
token_vk = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

class DownloadsPhoto:

    def __init__(self, user_id: str, token_vk: str):
        self.user_id = user_id
        self.token_vk = token_vk
        self.direct = r'D:\PhotoVk'
    
    def downloads_photo_from_vk(self):
        # os.mkdir(self.direct)
        os.chdir(self.direct)
        url_vk = 'https://api.vk.com/method/photos.get'
        params_vk = {
        'owner_id': self.user_id,
        'album_id': 'profile',
        'extended': '1',
        'access_token': self.token_vk,
        'v':'5.131'
    }
        res = requests.get(url_vk, params=params_vk)
        bar = Bar('Скачивание фото', max=len(res.json()['response']['items']))
        list_name_fils_by_likes = []
        list_name_fils_by_date = []
        for i in res.json()['response']['items']:
            list_name_fils_by_likes.append(i['likes']['count'])
            list_name_fils_by_date.append(i['date'])
            url_photo = i['sizes'][-1]['url']
            self.size = i['sizes'][-1]['type']
            new_list_name = []
            for i, char in enumerate(list_name_fils_by_likes):
                if char not in new_list_name:
                    new_list_name.append(char)
                else:
                    list_name_fils_by_likes[i] = list_name_fils_by_date[i]
            response = requests.get(url_photo)
            for name in list_name_fils_by_likes:
                continue
            with open(f"{name}.jpg", "wb") as f:
                f.write(response.content)
                bar.next()
                time.sleep(1)
            logs_list = []
            download_log = {'file_name': name, 'size': self.size}
            logs_list.append(download_log)
            with open(f'{self.direct}/log.json', 'a') as file:
                json.dump(logs_list, file, indent=2)


if __name__ == '__main__':
    user1 = DownloadsPhoto(id, token_vk)
    user1.downloads_photo_from_vk()



