import vk_api
import time

from config import vk_token_main, vk_token_beta, mySQL

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


    base = _botdb(
        host=mySQL["server"],
        username=mySQL["username"],
        secret=mySQL["password"], 
        db_name=mySQL["db_name"]
    )

    def send_message(user_id, message, keyboard=None):
        post = {
            "user_id": user_id,
            "message": message,
            "random_id": 0
        }
        if keyboard != None:
            post["keyboard"] = keyboard.get_keyboard()

        session.method("messages.send", post)

    def send_schedule(x, style):
        send_message(user_id, "Уже ищу", None)
        spisok = request.array()
        if (base.column_info(3, user_id) == "без картинок"):
            send_message(user_id, f"Держи ссылку на расписание: \n{spisok[x]}.")
        else:
            send_message(user_id, f"Держи ссылку на расписание: \n{spisok[x]} \n\nВ течение минуты пришлю дополнительно картинки с расписанием")
            request.download_convert(x, style, user_id)
            send_message(user_id, f"На этом пока все!")

    ### ---------------- доп параметры ------------------- ###
    album_id = 281423879
    group_id = 207687870

    dev1_id = 206507284
    dev2_id = 200496247

    k = 0

    err_mes_user = 1

    dev1_alerts = 0
    dev2_alerts = 0

    dev1_err_mes_user = 0
    dev2_err_mes_user = 0

    privet = "0E2C2F0E2F190E2E210E2E1B0E2E1E0E2F1B"

    main_ui_position = "расписание", "полезные ссылки", "навигация 1", "игры", "настройки", "контакты преподавателей"
    course_ui_position = "1 курс", "2 курс", "3 курс", "4 курс"
    ### ------------------------------------------------- ###

    for event in VkLongPoll(session).listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            text = event.text.lower()
            text_teacher = event.text
            user_id = event.user_id

            keyboard = VkKeyboard(one_time=False)

            if not base.user_id_exists(user_id):
                base.create_user(user_id)
                print(f"Появился новый пользователь! ID: {user_id}")

                kb.start(keyboard)
                send_message(user_id, data.start_message, keyboard)

            ### главное меню {"главное меню"}###
            elif (text == "начать") or (text == "start") or (text == "главное меню") or (base.column_info(2, user_id) in main_ui_position and text == "назад"):
                kb.main_menu(keyboard)
                send_message(user_id, "Главное меню", keyboard)

                base.set_position(user_id, "главное меню")


            ## расписание {"расписание"}##
            elif (text == "расписание") or (base.column_info(2, user_id) == "главное меню" and text == "📆 расписание") or (base.column_info(2, user_id) in course_ui_position and text == "назад"):
                kb.schedule(keyboard)
                send_message(user_id, "Выбери курс", keyboard)

                base.set_position(user_id, "расписание")

            # 1 курс {"1 курс"}#
            elif (base.column_info(2, user_id) == "расписание" and text == "1 курс"):
                send_message(user_id, "Подожди секундочку...")
                kb.FC_schedule(keyboard)
                send_message(user_id, "Смотри, что нашел: \n\n", keyboard)

                base.set_position(user_id, "1 курс")

            elif text == "экономика об-7350-21" or text == "об-7350-21" or text == "об735021":
                send_schedule(1, (base.column_info(3, user_id)))

            elif text == "цифровые технологии об-230766-21" or text == "об-230766-21" or text == "об23076621":
                send_schedule(3, (base.column_info(3, user_id)))
            elif text == "информационная безопасность об-7351-21" or text == "об-7351-21" or text == "об735121":
                send_schedule(2, (base.column_info(3, user_id)))

            # 2 курс {"2 курс"}#
            elif (base.column_info(2, user_id) == "расписание" and text == "2 курс"):
                send_message(user_id, "Подожди секундочку...")
                kb.SC_schedule(keyboard)
                send_message(user_id, "Смотри, что нашел: \n\n", keyboard)

                base.set_position(user_id, "2 курс")

            elif text == "экономика об-7350-20" or text == "об-7350-20" or text == "об735020":
                send_schedule(7, (base.column_info(3, user_id)))

            elif text == "информационная безопасность об-7351-20" or text == "об-7351-20" or text == "об735120":
                send_schedule(8, (base.column_info(3, user_id)))

            # 3 курс {"3 курс"}#
            elif (base.column_info(2, user_id) == "расписание" and text == "3 курс"):
                send_message(user_id, "Подожди секундочку...")
                kb.TC_schedule(keyboard)
                send_message(user_id, "Смотри, что нашел: \n\n", keyboard)

                base.set_position(user_id, "3 курс")

            elif text == "экономика об-7350-19" or text == "об-7350-19" or text == "об735019":
                send_schedule(11, (base.column_info(3, user_id)))

            elif text == "информационная безопасность об-7351-19" or text == "об-7351-19" or text == "об735119":
                send_schedule(12, (base.column_info(3, user_id)))

            # 4 курс {"4 курс"}#
            elif (base.column_info(2, user_id) == "расписание" and text == "4 курс"):
                send_message(user_id, "Подожди секундочку...")
                kb.FO_schedule(keyboard)
                send_message(user_id, "Смотри, что нашел: \n\n", keyboard)

                base.set_position(user_id, "4 курс")

            elif text == "экономика об-7350-18" or text == "об-7350-18" or text == "об735018":
                send_schedule(15, (base.column_info(3, user_id)))

            elif text == "информационная безопасность об-7351-18" or text == "об-7351-18" or text == "об735118":
                send_schedule(16, (base.column_info(3, user_id)))

            ## контакты ##
            elif (base.column_info(2, user_id) == "главное меню" and text == "📞 контакты преподавателей"):
                kb.contacts(keyboard)
                send_message(user_id, "контакты преподавателей", keyboard)

                base.set_position(user_id, "контакты преподавателей")

            elif (base.column_info(2, user_id) == "контакты преподавателей" and text == "посмотреть весь список"):
                send_message(user_id, data.contacti_pochta)

            elif (base.column_info(2, user_id) == "контакты преподавателей" and text == "поиск преподавателя"):
                send_message(user_id, data.serch_teach)

            elif (base.column_info(2, user_id) == "контакты преподавателей"):
                if base.teacher_exists(text.title()):
                    send_message(user_id, f"{base.teacher_info(1, text.title())} {base.teacher_info(0, text.title())} {base.teacher_info(2, text.title())} - {base.teacher_info(3, text.title())}")
                else:
                    send_message(user_id, "Я такого преподавателя пока не знаю.")

            ## время работы ##
            elif (base.column_info(2, user_id) == "главное меню" and text == "🕖 время работы"):
                send_message(user_id, data.time_work)

            ## полезные ссылки ##
            elif text == "🌐 полезные ссылки":
                kb.link(keyboard)
                send_message(user_id, data.usseful_sites, keyboard)

                base.set_position(user_id, "полезные ссылки")

            ## навигация по ранхигс {"навигация 1"}##
            elif (base.column_info(2, user_id) == "главное меню" and text == "🧭 навигация по ранхигс") or (base.column_info(2, user_id) == "навигация 2" and text == "назад"):
                kb.navigation(keyboard)
                send_message(user_id, "Что тебя интересует?", keyboard)

                base.set_position(user_id, "навигация 1")

            # поиск кабинета #
            elif (base.column_info(2, user_id) == "навигация 1" and text == "ищу кабинет"):
                send_message(user_id, data.serch_kab)

            # cхема кампуса #
            elif (base.column_info(2, user_id) == "навигация 1" and text == "схема кампуса"):
                send_message(user_id, "Держи схему терретории РАНХиГС:")
                navigation.send_kampus(user_id)

            # схема отдельного корпуса #
            elif (base.column_info(2, user_id) == "навигация 1" and text == "схема отдельного корпуса"):
                kb.scheme_housing(keyboard)
                send_message(user_id, "Выбери корпус:", keyboard)

                base.set_position(user_id, "навигация 2")

            # схема отдельного корпуса #
            elif ('/' in text and len(text) < 7):
                send_message(user_id, "Смотри, что нашел:")
                navigation.send_etaj(text, user_id)

            # схема отдельного корпуса #
            elif (base.column_info(2, user_id) == "навигация 2" and "корпус" in text):
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
            elif (base.column_info(2, user_id) == "главное меню" and text == "☁ погода"):
                send_message(user_id, request.weather_def())

            ## игры ##
            elif (base.column_info(2, user_id) == "главное меню" and text == "🔮 игры"):
                kb.games(keyboard)
                send_message(user_id, "Смотри какие игры я знаю:", keyboard)

                base.set_position(user_id, "игры")

            ## настройки ##
            elif (base.column_info(2, user_id) == "главное меню" and text == "⚙ настройки") or (base.column_info(2, user_id) == "настройки стиль" and text == "назад"):
                kb.settings(keyboard, (base.column_info(3, user_id)))
                send_message(user_id, "Меню настроек", keyboard)

                base.set_position(user_id, "настройки")

            elif (base.column_info(2, user_id) == "настройки" and "стиль" in text):
                kb.style_settings(keyboard, (base.column_info(3, user_id)))
                send_message(user_id, "Выбери стиль расписания:", keyboard)

                base.set_position(user_id, "настройки стиль")

            elif (base.column_info(2, user_id) == "настройки стиль"):
                style_count = 0
                if ("классический" in text):
                    base.set_type_of_schedule(user_id, "классический")
                    kb.style_settings(keyboard, (base.column_info(3, user_id)))

                elif("упрощенный" in text):
                    base.set_type_of_schedule(user_id, "упрощенный")
                    kb.style_settings(keyboard, (base.column_info(3, user_id)))

                elif("без картинок" in text):
                    base.set_type_of_schedule(user_id, "без картинок")
                    kb.style_settings(keyboard, (base.column_info(3, user_id)))
                    style_count = 1

                if style_count == 0:
                    send_message(user_id, f"Выбран {base.column_info(3, user_id)} стиль", keyboard)
                elif style_count == 1:
                    send_message(user_id, f"Выбран стиль {base.column_info(3, user_id)}", keyboard)

            # идея / сообщить об ошибке #
            elif (base.column_info(2, user_id) == "настройки" and text == "💡 идея / 🤔 сообщить об ошибке"):
                k += 1
                send_message(user_id, "Напишите вашу идею или найденную ошибку. Я передам информацию разработчикам, что ты хочем им что-то сообщить")

                if dev1_alerts == 1:
                    send_message(dev1_id, f"💡 {user_id}")

                if dev2_alerts == 1:
                    send_message(dev2_id, f"💡 {user_id}")

            # о боте #
            elif (base.column_info(2, user_id) == "настройки" and text == "🤖 о боте"):
                send_message(user_id, data.o_bote)

            # вопросы / ответы #
            elif (base.column_info(2, user_id) == "настройки" and text == "❓ f.a.q."):
                send_message(user_id, data.faq)

            # анекдот #
            elif (text == "анекдот"):
                send_message(user_id, "Помню я один анекдот, сейчас расскажу...")
                send_message(user_id, request.joke_def())

            ## dev ##
            elif (base.column_info(2, user_id) == "настройки" and base.column_info(1, user_id) == "owner" and text == "dev"):
                kb.developer(keyboard)
                send_message(user_id, privet, keyboard)

                base.set_position(user_id, "aдмин панель")

            elif (base.column_info(2, user_id) == "aдмин панель" and base.column_info(1, user_id) == "owner"):

                if "err_mes_user" in text:
                    if "вкл" in text:
                        err_mes_user = 1

                        send_message(user_id, "err_mes_user вкл")

                    elif "выкл" in text:
                        err_mes_user = 0

                        send_message(user_id, "err_mes_user выкл")

            elif (err_mes_user == 1):
                send_message(user_id, "Не совсем понимаю, что ты хочешь сказать\nВыбери пункт в меню.\n\n Если нничего не получается, то просто напиши команду 'начать' или 'start' ")

            base.message_count(user_id)
            time.sleep(0.5)



vk_token = select_token()

def main_restart():
    try:
        main()
    except Exception as err:
        print(err)
        time.sleep(1)
        main_restart()


main_restart()

# main()
