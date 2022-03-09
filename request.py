import requests as req
import vk_api
from bs4 import BeautifulSoup as bs
import convertapi
import os
import os.path
from config import convert_token, vk_token

convertapi.api_secret = convert_token

session = vk_api.VkApi(token = vk_token)
session_api = session.get_api()

#### достаем шутки ####
def joke_def():
    joke_res = req.get('https://v2.jokeapi.dev/joke/Programming?type=single')

    joke = joke_res.json()['joke']

    joke_exit = (
        joke
    )

    return(joke_exit)

#### достаем ссылки на расписания ####
def array():
    arr = []

    res = req.get('http://emit.ranepa.ru/faculty-2/ai/')

    html = res.text
    soup = bs(html, 'html.parser')
    elems = soup.select('.col-6.col-md-6.col-lg-4.p-0 a')

    for elem in elems:
        arr.append(elem['href'])

    ## print(arr)
    return(arr)

#### отправка фотографий ####
def send_photo(photo, user_id):
    a = session.method('photos.getMessagesUploadServer')
    b = req.post(a['upload_url'], files={'photo': open(photo, 'rb')}).json()
    c = session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    d = 'photo{}_{}'.format(c['owner_id'], c['id'])

    post = {'user_id': user_id, 'attachment': d, "random_id": 0}

    session.method('messages.send', post)

#### конфертируем пдф в пнг ####
def download_convert(x, user_id):

    spisok = array()

    ### проверка папки, если есть, то удаляем ###
    check_file = os.path.exists("foto")

    if check_file == True:
        list = os.listdir("foto")

        for x in list:
            os.remove(f"foto/{x}")

        os.rmdir("foto")

    ### создаем папку вновь ###
    os.mkdir("foto")
    
    res = req.get(spisok[x])

    with open(f'{x}.pdf', 'wb') as f:
        f.write(res.content)

    convertapi.convert('png', {'File': f'{x}.pdf'}, from_format = 'pdf').save_files('foto')

    ### отсылаем сообщение ###
    send_photo(f"foto/{x}.png", user_id)
    #print(f"{os.path.abspath('')}/foto\{x}.png")

    for y in range(0, 5):

        check_file = os.path.exists(f"foto/{x}-{y}.png")

        if check_file == True:
            photo = f"foto/{x}-{y}.png"

            send_photo(photo, user_id)

    spisok = []

    list = os.listdir("foto")

    ### подчищаем хвосты после скаченных данных ###
    os.remove(f"{x}.pdf")

    for x in list:
        os.remove(f"foto/{x}")

    os.rmdir("foto")