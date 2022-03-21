import os
import os.path
import sqlite3
import pymysql
import vk_api
from pyowm import OWM
import requests as req
from config import owm_token
from bs4 import BeautifulSoup as bs
from pdf2image import convert_from_path
from pyowm.utils.config import get_default_config


class _request:
    def __init__(self, token):
        self.session = vk_api.VkApi(token = token)

    #### достаем шутки ####
    def joke_def(self):
        joke_res = req.get('https://v2.jokeapi.dev/joke/Programming?type=single')

        joke = joke_res.json()['joke']

        joke_exit = joke

        return(joke_exit)

    ### погода ###
    def weather_def(self):
        config_dict = get_default_config()
        config_dict['language'] = 'ru'

        place = "Moscow, RU"
        owm = OWM(owm_token, config_dict)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather

        t = w.temperature("celsius")
        t1 = t['temp']
        t2 = t['feels_like']
        wi = w.wind()['speed']
        humi = w.humidity
        dt = w.detailed_status

        weather_exit = (
            f"На данный момент погода: \n\n"
            f"🌡&#4448;Tемпература:&#4448;{round(t1)} °C \n"
            f"👅&#4448;Ощущается как:&#4448;{round(t2)} °C \n"
            f"💨&#4448;Скорость ветра:&#4448;{wi} м/с \n"
            f"💧&#4448;Влажность:&#4448;{humi}% \n"
        )

        return(weather_exit)

    #### достаем ссылки на расписания ####
    def array(self):
        arr = []

        res = req.get('http://emit.ranepa.ru/faculty-2/ai/')

        html = res.text
        soup = bs(html, 'html.parser')
        elems = soup.select('.col-6.col-md-6.col-lg-4.p-0 a')

        for elem in elems:
            arr.append(elem['href'])

        return(arr)

    #### отправка фотографий ####
    def send_photo(self, photo, user_id):
        a = self.session.method('photos.getMessagesUploadServer')
        b = req.post(a['upload_url'], files={'photo': open(photo, 'rb')}).json()
        c = self.session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
        d = 'photo{}_{}'.format(c['owner_id'], c['id'])

        post = {'user_id': user_id, 'attachment': d, "random_id": 0}

        self.session.method('messages.send', post)

    def send_photo_patchka(self, photo, user_id):
        a = self.session.method('photos.getMessagesUploadServer')
        b = req.post(a['upload_url'], files={'photo': open(photo, 'rb')}).json()
        c = self.session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
        d = 'photo{}_{}'.format(c['owner_id'], c['id'])

        post = {'user_id': user_id, 'attachment': d, "random_id": 0}

        self.session.method('messages.send', post)

    #### конфертируем пдф в пнг ####
    def download_convert(self, x, style, user_id):

        spisok = self.array()

        ### проверка папки, если есть, то удаляем ###
        check_file = os.path.exists("foto")

        if check_file == True:
            list = os.listdir("foto")

            for y in list:
                os.remove(f"foto/{y}")

            os.rmdir("foto")

        ### создаем папку вновь ###
        os.mkdir("foto")

        res = req.get(spisok[x])

        with open(f'{x}.pdf', 'wb') as f:
            f.write(res.content)

        def convert_to_pdf(self, style, pdf):
            pages = convert_from_path(pdf, 100)

            for i, page in enumerate(pages):
                page.save(f'foto/{i}.png', 'PNG')
                count = i

                if style == "классический":
                    self.send_photo(f"foto/{i}.png", user_id)

            if style == "упрощенный":
                count += 1
                fotos = []
                fotos_exit = ""

                for i in range(0, count):

                    a = self.session.method('photos.getMessagesUploadServer')
                    b = req.post(a['upload_url'], files={'photo': open(f"foto/{i}.png", 'rb')}).json()
                    c = self.session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                    d = 'photo{}_{}'.format(c['owner_id'], c['id'])

                    fotos.append(d)

                    if i == 0:
                        fotos_exit = fotos[i]
                    else:
                        fotos_exit = fotos_exit + "," + fotos[i]

                post = {'user_id': user_id,'attachment': f'{fotos_exit}', "random_id": 0}

                self.session.method('messages.send', post)

        convert_to_pdf(self, style,f'{x}.pdf')

        spisok = []

        list = os.listdir("foto")

        ### подчищаем хвосты после скаченных данных ###
        os.remove(f"{x}.pdf")

        for y in list:
            os.remove(f"foto/{y}")

        os.rmdir("foto")

class _navigation:
    def __init__(self, token):
        self.session = vk_api.VkApi(token=token)

    def send_photo(self, photo, user_id):
        a = self.session.method('photos.getMessagesUploadServer')
        b = req.post(a['upload_url'], files={'photo': open(photo, 'rb')}).json()
        c = self.session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
        d = 'photo{}_{}'.format(c['owner_id'], c['id'])

        post = {'user_id': user_id, 'attachment': d, "random_id": 0}

        self.session.method('messages.send', post)

    def send_kampus(self, user_id):
        self.send_photo(f"navi/kampus.jpg", user_id)


    def getLocation(adress):
        [room, building] = adress.split("/")
        return {
            'floor': room[0],
            'building': building,
            'title': building + "_" + room[0]
        }


    def send_etaj(self, adress, user_id):
        self.send_photo(f"navi/{_navigation.getLocation(adress).get('building')}/{_navigation.getLocation(adress).get('title')}.jpg", user_id)

    def send_korpus(self, build, user_id):

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
            self.send_photo(f"navi/{build}/{build}_{x}.jpg", user_id)
            x = x + 1


class _botdb:
    def __init__(self, host, username, secret, db_name):
        self.conn = pymysql.connect(
            host=host,
            user=username,
            password=secret,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset="utf8"
        )

        # self.conn = sqlite3.connect(db_name)

        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                user_id INT,
                role TEXT,
                ui_position TEXT,
                type_of_schedule TEXT,
                number_of_message INT
            ) CHARACTER SET utf8mb4;
        """)

        self.conn.commit()

    def user_id_exists(self, user_id):
        self.cur.execute(
            f"""SELECT * FROM users WHERE user_id LIKE {user_id}""")

        result = self.cur.fetchall()

        return(bool(result))

    def create_user(self, user_id):
        self.cur.execute(f"""INSERT INTO users (user_id, role, ui_position, type_of_schedule, number_of_message) VALUES ({user_id}, "user", "главное меню", "классический", {0})""")

        self.conn.commit()

    def set_position(self, user_id, position):
        self.cur.execute(f"""UPDATE users SET ui_position = "{position}" WHERE user_id = {user_id}""")

        self.conn.commit()

    def column_info(self, x,  user_id):
        self.cur.execute(f"""SELECT * FROM users WHERE user_id = {user_id}""")

        position=''

        if (x == 2):
            position = 'ui_position'
        elif (x == 3):
            position = 'type_of_schedule'
        elif (x == 4):
            position = 'number_of_message'
        
        info = self.cur.fetchone()[position]

        if not info:
            return ''
        
        return(info)

    def set_type_of_schedule(self, user_id, type):
        self.cur.execute(f"""UPDATE users SET type_of_schedule = "{type}" WHERE user_id = {user_id}""")

        self.conn.commit()

    def message_count(self, user_id):
        self.cur.execute(f"""SELECT number_of_message FROM users WHERE user_id = {user_id} """)

        new_count = self.cur.fetchall()[0]['number_of_message'] + 1

        self.cur.execute(f"""UPDATE users SET number_of_message = {new_count} WHERE user_id = {user_id}""")

        self.conn.commit()

    def teacher_exists(self, name):
        self.cur.execute(f"""SELECT * FROM teacher WHERE sname = "{name}" """)

        result = self.cur.fetchall()

        return(bool(result))

    def teacher_info(self, x, name):
        self.cur.execute(f"""SELECT * FROM teacher WHERE sname = "{name}" """)
         
        column=''

        if (x == 0):
            column = 'fname'
        elif (x == 1):
            column = 'sname'
        elif (x == 2):
            column = 'tname'
        elif (x == 3):
            column = 'mail'

        info = self.cur.fetchone()[column]

        return(info)
