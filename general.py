from distutils.log import info
import os
import os.path
from pickle import FALSE
import sqlite3
import vk_api
import time
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
        joke_res = req.get('https://v2.jokeapi.dev/joke/Programming?type=single', verify=False)

        joke = joke_res.json()['joke']

        joke_exit = joke

        return(joke_exit)

    def parse_google_sheets(self, id, sheet_name, range_req):
        res = req.get(
            f'https://script.google.com/macros/s/AKfycbx1bumTMdwKXfgqx16AbMo44RaVMF694TGxQ9ZHj2vJMPkpHu4TnnzWlF5G2Zn_5GeT/exec?id={id}&sheetName={sheet_name}&rangeReq={range_req}', verify=False)
        json_res = res.json()
        return(json_res)

    def naychnik_info(self):
        naychnik = self.parse_google_sheets('1GScYqi8PKwU8y2tNnP1QeVY0pMZsPxD18p_alkas93Q',
                                'Научники/консультанты',
                                            'C84:I93')
        result = ""
        naychryk = ""
        consul = ""

        for i in range(len(naychnik)):
            if (naychnik[i][3] == 1):
                naychryk = f"Осталось {15 - naychnik[i][1]} мест"
            else:
                naychryk = "нет"

            if (naychnik[i][4] == 1):
                consul = f"Осталось {15 - naychnik[i][2]} мест"
            else:
                consul = "нет"

            result += (f"{naychnik[i][0]}\nНаучное руководство: {naychryk}\nКонсультирование: {consul}\nПочта: {naychnik[i][5]}\n\n")

        return(result)



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

        res = req.get('http://emit.ranepa.ru/faculty-2/ai/', verify=False)

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

    def send_photo_restart(self, photo, user_id):
        try:
            self.send_photo(photo, user_id)
        except Exception:
            print(f"Ошибка G-SP-01 | user_id: {user_id}")
            time.sleep(1)
            self.send_photo_restart(photo, user_id)

    def send_photo_pachka(self, count, user_id):
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

    def send_photo_pachka_restart(self, count, user_id):
        try:
            self.send_photo_pachka(count, user_id)
        except Exception:
            print(f"Ошибка G-SP-02 | user_id: {user_id}")
            time.sleep(1)
            self.send_photo_pachka_restart(count, user_id)
        
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

        res = req.get(x, verify=False)

        with open("schedule.pdf", 'wb') as f:
            f.write(res.content)

        def convert_to_pdf(self, style, pdf):
            pages = convert_from_path(pdf, 100)

            for i, page in enumerate(pages):
                page.save(f'foto/{i}.png', 'PNG')
                count = i

                if style == "классический":
                    self.send_photo_restart(f"foto/{i}.png", user_id)

            if style == "упрощенный":
                self.send_photo_pachka_restart(count, user_id)

        convert_to_pdf(self, style, "schedule.pdf")

        spisok = []

        list = os.listdir("foto")

        ### подчищаем хвосты после скаченных данных ###
        os.remove("schedule.pdf")

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

    def send_photo_restart(self, photo, user_id):
        try:
            self.send_photo(photo, user_id)
        except Exception:
            print(f"Ошибка G-SP-03 | user_id: {user_id}")
            time.sleep(1)
            self.send_photo_restart(photo, user_id)


    def send_kampus(self, user_id):
        self.send_photo_restart(f"navi/kampus.jpg", user_id)

    def getLocation(adress):
        [room, building] = adress.split("/")
        return {
            'floor': room[0],
            'building': building,
            'title': building + "_" + room[0]
        }

    

    def send_etaj(self, adress, user_id):
        corpus = "1", "2", "3", "5", "6"
        if (_navigation.getLocation(adress).get('building') in corpus):
            self.send_photo_restart(f"navi/{_navigation.getLocation(adress).get('building')}/{_navigation.getLocation(adress).get('title')}.jpg", user_id)
        else:
            return 0
        

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
            self.send_photo_restart(f"navi/{build}/{build}_{x}.jpg", user_id)
            x = x + 1


class _botdb:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)

        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Schedule(
            S_ID INT,
            COURSE INT,
            F_EDU TEXT,
            S_LINK TEXT,
            S_NAME TEXT,
            S_NUM TEXT
        )""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Student(
            S_ID INT, 
            ROLE TEXT,
            COURSE TEXT,
            F_EDU TEXT,
            UI_POS TEXT,
            TYPE_SCH TEXT,
            MAIL TEXT,
            NUM_MES INT
            )""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Teachers(
            F_NAME TEXT,
            S_NAME TEXT,
            T_NAME TEXT,
            EMAIL TEXT
            )""")

        self.conn.commit()
    
    ## Студент ##
    def user_id_exists(self, user_id):
        self.cur.execute(
            f"""SELECT * FROM Student WHERE S_ID LIKE {user_id}""")

        result = self.cur.fetchall()

        return(bool(result))

    def create_user(self, user_id):
        self.cur.execute(
            f"""INSERT INTO Student (S_ID, ROLE, COURSE, F_EDU, UI_POS, TYPE_SCH, MAIL, NUM_MES) VALUES ({user_id}, "студент", "не указан", "не указан", "регистрация", "классический", "Да", {0})""")

        self.conn.commit()

    def set_position(self, user_id, position):
        self.cur.execute(
            f"""UPDATE Student SET UI_POS = "{position}" WHERE S_ID = {user_id}""")

        self.conn.commit()

    def set_type_of_schedule(self, user_id, type):
        self.cur.execute(
            f"""UPDATE Student SET TYPE_SCH = "{type}" WHERE S_ID = {user_id}""")

        self.conn.commit()

    def message_count(self, user_id):
        self.cur.execute(
            f"""SELECT NUM_MES FROM Student WHERE S_ID = {user_id} """)

        new_count = self.cur.fetchall()[0][0] + 1

        self.cur.execute(
            f"""UPDATE Student SET NUM_MES = {new_count} WHERE S_ID = {user_id}""")

        self.conn.commit()

    def update_forma(self, user_id, forma):
        self.cur.execute(
            f"""UPDATE Student SET F_EDU = "{forma}" WHERE S_ID = {user_id}""")

        self.conn.commit()

    def update_course(self, user_id, course):
        self.cur.execute(
            f"""UPDATE Student SET COURSE = "{course}" WHERE S_ID = {user_id}""")

        self.conn.commit()

    def sql_delete(self, user_id):
        self.cur.execute(
            f"""DELETE FROM Student WHERE S_ID = {user_id}""")

        self.conn.commit()

    def column_info(self, x,  user_id):
        self.cur.execute(
            f"""SELECT * FROM Student WHERE S_ID = {user_id}""")

        info = self.cur.fetchone()[x]

        return(info)

    def user_info(self, user_id):
        self.cur.execute(
            f"""SELECT * FROM Student WHERE S_ID = {user_id}""")

        info = self.cur.fetchone()

        return(info)

    ## Учителя ##
    def teacher_exists(self, name):
        self.cur.execute(
            f"""SELECT * FROM Teachers WHERE S_NAME = "{name}" """)

        result = self.cur.fetchall()

        return(bool(result))

    def teacher_info(self, x, name):
        self.cur.execute(
            f"""SELECT * FROM Teachers WHERE S_NAME = "{name}" """)
        info = self.cur.fetchone()[x]

        return(info)

    def get_all_teachers(self):
        text = ""
        self.cur.execute(
            f"""SELECT * FROM Teachers ORDER BY S_NAME""")

        rows = self.cur.fetchall()
        for row in rows:
            text += (f"""{str(row[1])} {str(row[0])} {str(row[2])}\n&#4448;&#4448;{str(row[3])}\n""")

        return(text)

    def count_teachers(self):
        self.cur.execute(
            f"""SELECT * FROM Teachers""")

        k = self.cur.fetchone()[0]

        return(k)

    ## Расписание ##
    def schedule_exists(self, user_id):
        course = self.column_info(2, user_id)
        form = self.column_info(3, user_id)

        self.cur.execute(
            f"""SELECT * FROM Schedule WHERE COURSE = "{course}" AND  F_EDU = "{form}" """)

        result = self.cur.fetchall()
        
        return(bool(result))

    def send_group_schedule(self, user_id):
        course = self.column_info(2, user_id)
        form = self.column_info(3, user_id)

        self.cur.execute(
            f"""SELECT * FROM Schedule WHERE COURSE = "{course}" AND  F_EDU = "{form}" """)

        result = self.cur.fetchall()

        info = []

        for row in result:
            info.append(row[4] + " " + row[5])

        return(info)

    def send_schedule(self, message):
        self.cur.execute(
            f"""SELECT * FROM Schedule""")
        
        schedules = self.cur.fetchall()

        schedules_num = []

        for row in schedules:
            schedules_num.append(row[5])

        schedule_row = -1

        for i, schedule_num in enumerate(schedules_num):
            if schedule_num in message:
                schedule_row = i

        if schedule_row == -1:
            return(False)

        schedule = schedules[schedule_row][3]

        return(schedule)

    ## Регистрация ##
    def reg(self, table, f_column, s_column, search):
        self.cur.execute(
            f"""SELECT {f_column} FROM {table} WHERE {s_column} = "{search}" """)

        info = self.cur.fetchall()

        result = []

        for row in info:
            result.append(row[0])

        return(result)