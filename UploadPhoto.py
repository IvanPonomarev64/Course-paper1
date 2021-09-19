import requests
import os
import time
from progress.bar import Bar


token_yandex = ''

class UploadPhoto:

    def __init__(self, token_yandex: str):
        self.token_yandex = token_yandex
        self.direct = r'D:\PhotoVk'
        self.number_of_files_to_send = 5

    def uploading_files_to_yandex_disk(self,path):
        os.chdir(self.direct)
        files_list = [name for name in os.listdir(self.direct) if name.endswith(".jpg")]
        bar = Bar('Отправление файлов на Я.диск', max=len(files_list))
        count = 0
        number_of_sent = 0
        for name_file in files_list:
            count += 1
            while count <= self.number_of_files_to_send:
                number_of_sent += 1
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'OAuth {self.token_yandex}'
                }
                params = {
                    'path': f'{path}/{name_file}',
                    'overwrite':True
                }
                upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
                response = requests.get(upload_url, headers=headers, params=params)
                href = response.json().get("href", "")
                response = requests.api.put(href, data=open(name_file, 'rb'), headers=headers)
                bar.next()
                time.sleep(0.5)
                break
        if number_of_sent in range(2,5):
            print(f'\nНа Я.диск отправлено: {number_of_sent} файла')
        elif number_of_sent in range(5,21) or number_of_sent == 0:
            print(f'\nНа Я.диск отправлено: {number_of_sent} файлов')
        elif number_of_sent == 1 or number_of_sent == 21:
            print(f'\nНа Я.диск отправлен: {number_of_sent} файл')
            
    def creating_a_new_folder_on_yandex_disk(self, name_folder: str):
        headers = {
            "Accept": 'application/json',
            'Authorization': f'OAuth {self.token_yandex}'
        }
        params = {
            'path': f'/{name_folder}',  
        }
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        requests.put(upload_url, headers=headers, params=params)
        return name_folder


if __name__ == '__main__':
    user1 = UploadPhoto(token_yandex)
    user1.uploading_files_to_yandex_disk(user1.creating_a_new_folder_on_yandex_disk('Фотки с Vk'))
    # user1.creating_a_new_folder_on_yandex_disk('Фотки с Vk')