from pymysql import NULL
import vk_api
import time
import traceback

from config import vk_token_main, vk_token_beta

from vk_api.keyboard import VkKeyboard
from vk_api.longpoll import VkLongPoll, VkEventType

from data import _data as data
from keyboard import _keyboard as kb
from general import _request, _navigation, _botdb


def select_token():
    token = input("Куда подключаемся? \nНапиши main или beta \n>>")

    if token == "main":
        print("Основной бот запущен")
        return(vk_token_main)

    elif token == "beta":
        print("Тестовый бот запущен")
        return(vk_token_beta)

    else:
        print("ошибка")
        exit()

def main():
    session = vk_api.VkApi(token=vk_token)
    session_api = session.get_api()

    request = _request(vk_token)
    navigation = _navigation(vk_token)

    base = _botdb("base.db")

    def send_message(user_id, message, keyboard=None):
        post = {
            "user_id": user_id,
            "message": message,
            "random_id": 0
        }
        if keyboard != None:
            post["keyboard"] = keyboard.get_keyboard()

        session.method("messages.send", post)

    def send_schedule(x, user_id, style):
        send_message(user_id, "Уже ищу", None)
        spisok = request.array()
        
        h = x
        link = ""
        for i in spisok:
            if h in i:
                link = i

        if (base.column_info(5, user_id) == "без картинок"):
            send_message(user_id, f"Держи ссылку на расписание: \n{link}.")
            send_message(user_id, f"На этом пока все!")
        else:
            send_message(user_id, f"Держи ссылку на расписание: \n{link} \n\nВ течение минуты пришлю дополнительно картинки с расписанием")
            request.download_convert(link, style, user_id)
            send_message(user_id, f"На этом пока все!")

    ### ---------------- доп параметры ------------------- ###
    album_id = 281423879
    group_id = 207687870

    dev1_id = 206507284
    dev2_id = 200496247

    err_mes_user = 1

    dev1_alerts = 0
    dev2_alerts = 0

    dev1_err_mes_user = 0
    dev2_err_mes_user = 0

    privet = "Привет отец!"

    main_ui_position = "расписание", "полезные ссылки", "навигация 1", "игры", "настройки", "контакты преподавателей", "время работы", "меню выпускник"
    profile_ui_position = "настройки стиль", "настройки курс", "настройки форма"
    course_info = "1 курс", "2 курс", "3 курс", "4 курс", "5 курс", "1 курс Магистратура", "2 курс Магистратура"
    forma_info = "Очная форма", "Очно-заочная форма"
    
    ### ------------------------------------------------- ###

    for event in VkLongPoll(session).listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            text = event.text.lower()
            text_standart = event.text
            user_id = event.user_id

            keyboard = VkKeyboard(one_time=False)

            if not base.user_id_exists(user_id):
                base.create_user(user_id)
                print(f"Появился новый пользователь! ID: {user_id}")

                kb.start(keyboard)
                send_message(user_id, data.start_message, keyboard)
                
                base.set_position(user_id, "регистрация")

            #### Регистрация ####
            elif (base.column_info(4, user_id) == "регистрация" and text == "приступить к работе"):
                kb.course(keyboard, base.user_info(user_id))
                send_message(user_id, "Для начала помоги мне и выбери курс на котором ты учишься, чтобы все функции работали стабильно.", keyboard)

                base.set_position(user_id, "регистрация курса")

            elif (base.column_info(4, user_id) == "регистрация курса" and text_standart in course_info):
                base.update_course(user_id, text_standart)
                kb.forma(keyboard, base.user_info(user_id))
                send_message(user_id, "Теперь выбери форму обучения", keyboard)

                base.set_position(user_id, "регистрация формы")

            elif (base.column_info(4, user_id) == "регистрация формы" and text_standart in forma_info):
                base.update_forma(user_id, text_standart)

                kb.main_menu(keyboard, base.user_info(user_id))
                send_message(
                    user_id, "Изменить выбранный курс и форму обучения ты сможешь в настройках. \n\n Добро пожаловать в Главное меню!", keyboard)

                base.set_position(user_id, "главное меню")

            ### главное меню {"главное меню"}###
            elif (text == "начать") or (text == "start") or (text == "главное меню") or (base.column_info(4, user_id) in main_ui_position and text == "назад"):
                kb.main_menu(keyboard, base.user_info(user_id))
                send_message(user_id, "Главное меню", keyboard)

                base.set_position(user_id, "главное меню")

            ## расписание {"расписание"}##
            elif (text == "расписание") or (base.column_info(4, user_id) == "главное меню" and text == "📆 расписание"):
                send_message(user_id, "Подожди секундочку...")
                if not base.schedule_exists(user_id):
                        send_message(user_id, "Твое расписание еще не появилось :(")
                else:
                    kb.gen_schedule(keyboard, base.send_group_schedule(user_id))
                    send_message(user_id, "Смотри, что нашел: \n\n", keyboard)
                    base.set_position(user_id, "расписание")

            ## контакты ##
            elif (base.column_info(4, user_id) == "главное меню" and text == "📞 контакты преподавателей"):
                kb.contacts(keyboard)   
                send_message(user_id, "Напиши мне фамилию преподавателя, который тебя интересует или просто посмотри список тех о ком я знаю.", keyboard)

                base.set_position(user_id, "контакты преподавателей")

            elif (base.column_info(4, user_id) == "контакты преподавателей" and text == "📋 посмотреть весь список"):
                send_message(user_id, base.get_all_teachers())

            elif (base.column_info(4, user_id) == "контакты преподавателей" and text == "🔍 поиск преподавателя"):
                send_message(user_id, data.serch_teach)

            elif (base.column_info(4, user_id) == "контакты преподавателей"):
                if base.teacher_exists(text.title()):
                    send_message(user_id, f"{base.teacher_info(1, text.title())} {base.teacher_info(0, text.title())} {base.teacher_info(2, text.title())} - {base.teacher_info(3, text.title())}")
                else:
                    send_message(user_id, "Я такого преподавателя пока не знаю.")

            # elif (base.column_info(4, user_id) == "главное меню" and text == "👨‍🎓 для выпускников"):
            #     kb.vipusk(keyboard)
            #     send_message(user_id, "Тут ты можешь найти информацию для выпускников.", keyboard)

            #     base.set_position(user_id, "меню выпускник")

            elif (base.column_info(4, user_id) == "главное меню" and text == "👨‍🎓 для выпускников"):
                send_message(user_id, "Скоро тут будет много интересного!")

            ## время работы ##
            elif (base.column_info(4, user_id) == "главное меню" and text == "🕖 часы работы"):
                kb.work_time(keyboard)
                send_message(user_id, "🕧", keyboard)

                base.set_position(user_id, "время работы")

            elif (base.column_info(4, user_id) == "время работы" and text == "💼 деканат"):
                send_message(user_id, data.dekanat_time)

            elif (base.column_info(4, user_id) == "время работы" and text == "🍕 точки питания"):
                send_message(user_id, data.tochki_food)
            
            elif (base.column_info(4, user_id) == "время работы" and text == "🚑 медицинский центр ранхигс"):
                send_message(user_id, data.med_work)

            ## полезные ссылки ##
            elif text == "🌐 полезные ссылки":
                kb.link(keyboard)
                send_message(user_id, data.usseful_sites, keyboard)

                base.set_position(user_id, "полезные ссылки")

            ## учебные материалы ##
            elif text == "📚 учебные материалы":
                send_message(user_id, data.edu_materials)

            ## навигация по ранхигс {"навигация 1"}##
            elif (base.column_info(4, user_id) == "главное меню" and text == "🧭 навигация по ранхигс") or (base.column_info(4, user_id) == "навигация 2" and text == "назад"):
                kb.navigation(keyboard)
                send_message(user_id, "Что тебя интересует?", keyboard)

                base.set_position(user_id, "навигация 1")

            # поиск кабинета #
            elif (base.column_info(4, user_id) == "навигация 1" and text == "ищу кабинет"):
                send_message(user_id, data.serch_kab)

            # cхема кампуса #
            elif (base.column_info(4, user_id) == "навигация 1" and text == "схема кампуса"):
                send_message(user_id, "Держи схему территории РАНХиГС:")
                navigation.send_kampus(user_id)

            # схема отдельного корпуса #
            elif (base.column_info(4, user_id) == "навигация 1" and text == "схема отдельного корпуса"):
                kb.scheme_housing(keyboard)
                send_message(user_id, "Выбери корпус:", keyboard)

                base.set_position(user_id, "навигация 2")

            # схема отдельного корпуса #
            elif ('/' in text and len(text) < 7):
                send_message(user_id, "Смотри, что нашел:")
                navigation.send_etaj(text, user_id)

            # схема отдельного корпуса #
            elif (base.column_info(4, user_id) == "навигация 2" and "корпус" in text):
                send_message(user_id, "Смотри, что нашел:")
                if "1" in text:
                    navigation.send_korpus(1, user_id)
                elif "2" in text:
                    navigation.send_korpus(2, user_id)
                elif "3" in text:
                    navigation.send_korpus(3, user_id)
                elif "5" in text:
                    navigation.send_korpus(5, user_id)
                elif "6" in text:
                    navigation.send_korpus(6, user_id)
                send_message(user_id, "На этом все.")

            ## погода ##
            elif (base.column_info(4, user_id) == "главное меню" and text == "☁ погода"):
                send_message(user_id, request.weather_def())

            ## настройки ##
            elif (base.column_info(4, user_id) == "главное меню" and text == "⚙ настройки") or (base.column_info(4, user_id) == "настройки профиля" and text == "назад"):
                kb.settings(keyboard)
                send_message(user_id, "Меню настроек", keyboard)

                base.set_position(user_id, "настройки")

            ## настройки профиля ##
            elif (base.column_info(4, user_id) == "настройки" and text == "📋 настройки профиля") or (base.column_info(4, user_id) in profile_ui_position and text == "назад"):
                kb.profile(keyboard, base.user_info(user_id))
                send_message(user_id, "Меню настроек профиля", keyboard)

                base.set_position(user_id, "настройки профиля")

            elif (base.column_info(4, user_id) == "настройки профиля" and "Курс:" in text_standart):
                kb.course(keyboard, base.user_info(user_id))
                send_message(user_id, "Выбери курс", keyboard)

                base.set_position(user_id, "настройки курс")

            elif (base.column_info(4, user_id) == "настройки профиля" and "Форма обучения:" in text_standart):
                kb.forma(keyboard, base.user_info(user_id))
                send_message(user_id, "Выбери форму", keyboard)

                base.set_position(user_id, "настройки форма")


            elif (base.column_info(4, user_id) == "настройки курс" and text_standart in course_info):
                base.update_course(user_id, text_standart)
                kb.profile(keyboard, base.user_info(user_id))

                if text_standart != "1 курс Магистратура" or text_standart != "2 курс Магистратура":
                    send_message(user_id, f"Выбран {text_standart} курс", keyboard)
                else:
                    send_message(user_id, f"Выбран {text_standart}", keyboard)

                base.set_position(user_id, "настройки профиля")

            elif (base.column_info(4, user_id) == "настройки форма" and text_standart in forma_info):
                base.update_forma(user_id, text_standart)
                kb.profile(keyboard, base.user_info(user_id))

                send_message(user_id, f"Выбрана {text_standart} форма", keyboard)

                base.set_position(user_id, "настройки профиля")
            

            # настройки стиля #
            elif (base.column_info(4, user_id) == "настройки профиля" and "стиль" in text):
                kb.style_settings(keyboard, base.column_info(5, user_id))
                send_message(user_id, "Выбери стиль расписания:", keyboard)

                base.set_position(user_id, "настройки стиль")

            elif (base.column_info(4, user_id) == "настройки стиль"):

                style_count = 0
                if ("классический" in text):
                    base.set_type_of_schedule(user_id, "классический")
                    kb.style_settings(keyboard, base.column_info(5, user_id))

                elif("упрощенный" in text):
                    base.set_type_of_schedule(user_id, "упрощенный")
                    kb.style_settings(keyboard, base.column_info(5, user_id))

                elif("без картинок" in text):
                    base.set_type_of_schedule(user_id, "без картинок")
                    kb.style_settings(keyboard, base.column_info(5, user_id))
                    style_count = 1

                if style_count == 0:
                    send_message(user_id, f"Выбран {base.column_info(5, user_id)} стиль", keyboard)
                elif style_count == 1:
                    send_message(user_id, f"Выбран стиль {base.column_info(5, user_id)}", keyboard)

            # идея / сообщить об ошибке #
            elif (base.column_info(4, user_id) == "настройки" and text == "💡 идея / 🤔 сообщить об ошибке"):
                send_message(user_id, data.idea_mistake)

            # о боте #
            elif (base.column_info(4, user_id) == "настройки" and text == "🤖 о боте"):
                send_message(user_id, data.o_bote)

            # вопросы / ответы #
            elif (base.column_info(4, user_id) == "настройки" and text == "❓ f.a.q."):
                send_message(user_id, data.faq)

            # идея/ошибка #
            elif ("идея: " in text or "ошибка: " in text):
                send_message(user_id, "Я передал ваше сообщение разработчикам")
                send_message(206507284, f"{user_id} | {text}")

            ## игры ##
            elif (text == "🔮 игры"):
                kb.games(keyboard)
                send_message(user_id, "Смотри какие игры я знаю:", keyboard)

                base.set_position(user_id, "игры")


            ## dev ##
            elif (base.column_info(1, user_id) == "разработчик" and (text == "dev")):
                kb.developer(keyboard)
                send_message(user_id, privet, keyboard)

                base.set_position(user_id, "aдмин панель")

            elif (base.column_info(4, user_id) == "aдмин панель" and base.column_info(1, user_id) == "разработчик"):

                if "err_mes_user" in text:
                    if "вкл" in text:
                        err_mes_user = 1

                        send_message(user_id, "err_mes_user вкл")

                    elif "выкл" in text:
                        err_mes_user = 0

                        send_message(user_id, "err_mes_user выкл")

                elif "удалить" in text:
                    delet_id = text.split(" ")

                    base.sql_delete(delet_id[1])

                    send_message(user_id, f"Пользователь с id{delet_id[1]} удален")

                elif text == "вызвать начальное сообщение":
                    send_message(user_id, data.start_message)


            ## =========== ПАСХАЛКИ =========== ##
            # анекдот #
            elif (text == "анекдот"):
                send_message(
                    user_id, "Помню я один анекдот, сейчас расскажу...")
                send_message(user_id, request.joke_def())
            ## =========== ПАСХАЛКИ =========== ##


            elif (err_mes_user == 1):
                
                schedule = base.send_schedule(text)

                if not schedule:
                    send_message(user_id, "Не совсем понимаю, что ты хочешь сказать\nВыбери пункт в меню.\n\n Если нничего не получается, то просто напиши команду 'начать', 'start' или 'главное меню' ")
                else:
                    send_schedule(schedule, user_id, base.column_info(5, user_id))
                        
                        
            base.message_count(user_id)
            time.sleep(0.2)

vk_token = select_token()

def main_restart():
    try:
        main()
    except Exception as err:
        print('========================')
        print(err)
        print('========================')
        print('Ошибка:\n', traceback.format_exc())
        print('========================')
        time.sleep(1)
        main_restart()


main_restart()

# main()
