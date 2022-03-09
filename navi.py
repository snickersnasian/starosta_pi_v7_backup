import requests as req
import vk_api
import os
import os.path
from config import vk_token

session = vk_api.VkApi(token = vk_token)
session_api = session.get_api()

#### отправка фотографий ####
def send_photo(photo, user_id):
    a = session.method('photos.getMessagesUploadServer')
    b = req.post(a['upload_url'], files={'photo': open(photo, 'rb')}).json()
    c = session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    d = 'photo{}_{}'.format(c['owner_id'], c['id'])

    post = {'user_id': user_id, 'attachment': d, "random_id": 0}

    session.method('messages.send', post)

def send_kampus(user_id):
    send_photo(f"navi/kampus.jpg", user_id)

def getLocation(adress):
    [room, building] = adress.split("/")
    return {
        'floor': room[0],
        'building': building,
        'title': building + "_" + room[0]
    }

def send_etaj(adress, user_id):
    send_photo(f"navi/{getLocation(adress).get('building')}/{getLocation(adress).get('title')}.jpg", user_id)

def send_korpus(build, user_id):
    list = os.listdir(f"navi/{build}")

    if build == 1:
        k = 3
    elif build == 2:
        k = 2
    elif build == 3:
        k = 4
    elif build == 5:
        k = 6
    elif build == 6:
        k = 3
        

    x = 1

    while x <= k:
        send_photo(f"navi/{build}/{build}_{x}.jpg",user_id)
        x = x + 1