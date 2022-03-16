### берем токен ###
import vk_api
from general import _request, _navigation, _botdb
from config import vk_token_main, vk_token_beta

def select_token():
    token = input("Куда подключаемся? \nНапиши main или beta \n>>")

    if token == "main":
        print("Основной бот запущен")
        return(vk_token_main)

    elif token == "beta":
        print("Тестовый бот запущен")
        return(vk_token_beta)
    
    elif token == None:
        print("ошибка")
        select_token()

    else:
        print("ошибка")
        select_token()

vk_token = select_token()

##### импорт #####

import time

##### достаем клавиатуру и longpoll #####
from vk_api.keyboard import VkKeyboard
from vk_api.longpoll import VkLongPoll, VkEventType

##### достаем из доп. файлов нужную информацию #####
from data import contacti_pochta, cool_sites, o_bote, faq, time_work, serch_kab
from keyboard import main_kb, set_kb, game_kb, link_kb, schedule_kb, materials_kb, navi_kb, sok_kb, dev_kb, FC_schedule_kb, SC_schedule_kb, TC_schedule_kb, FO_schedule_kb



#### главный процесс ####
def main():
    ### содаем сеcсию ###
    
    session = vk_api.VkApi(token=vk_token)
    session_api = session.get_api()
    request = _request(vk_token)
    navigation = _navigation(vk_token)

    ### функция для отправки сообщений ###
    def send_message(user_id, message, keyboard=None):
        post = {
            "user_id": user_id,
            "message": message,
            "random_id": 0
        }
        if keyboard != None:
            post["keyboard"] = keyboard.get_keyboard()

        session.method("messages.send", post)

    ### функция для отправки расписания ###
    def send_schedule(x):
        send_message(user_id, "Уже ищу", None)
        spisok = request.array()
        send_message(user_id, f"Держи ссылку на расписание: \n{spisok[x]} \n\nВ течение минуты пришлю дополнительно картинки с расписанием", None)
        request.download_convert(x, user_id)
        send_message(user_id, f"На всякий случай держи ссылку еще раз: \n{spisok[x]}", None)

    ### доп параметры ###
    album_id = 281423879
    group_id = 207687870

    dev1_id = 206507284
    dev2_id = 200496247

    k = 0

    dev1_alerts = 0
    dev2_alerts = 0

    privet = "0E2C2F0E2F190E2E210E2E1B0E2E1E0E2F1B"

    #Создаем ивент на сообщение
    for event in VkLongPoll(session).listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            text = event.text.lower()
            user_id = event.user_id

            keyboard = VkKeyboard(one_time=False)

            ### главное меню ###
            if text == "начать" or text == "start" or text == "назад" or text == "назад в главное меню" or text == "главное меню":
                main_kb(keyboard)
                send_message(user_id, "Главное меню", keyboard)

            ## расписание ##
            elif text == "📆 расписание" or text == "расписание" or text == "назад к выбору курса":
                schedule_kb(keyboard)
                send_message(user_id, "Выбери курс", keyboard)

            # 1 курс #
            elif text == "1 курс":
                send_message(user_id, "Подожди секундочку...")
                FC_schedule_kb(keyboard)
                send_message(user_id, "Смотри, что нашел: \n\n", keyboard)

            elif text == "экономика об-7350-21" or text == "об-7350-21" or text == "об735021":
                send_schedule(1)
                FC_schedule_kb(keyboard)
                send_message(user_id, f"На этом пока все!", keyboard)

            elif text == "цифровые технологии об-230766-21" or text == "об-230766-21" or text == "об23076621":
                send_schedule(3)
                FC_schedule_kb(keyboard)
                send_message(user_id, f"На этом пока все!", keyboard)

            elif text == "информационная безопасность об-7351-21" or text == "об-7351-21" or text == "об735121":
                send_schedule(2)
                FC_schedule_kb(keyboard)
                send_message(user_id, f"На этом пока все!", keyboard)

            # 2 курс #
            elif text == "2 курс":
                send_message(user_id, "Подожди секундочку...")
                SC_schedule_kb(keyboard)
                send_message(user_id, "Смотри, что нашел: \n\n", keyboard)

            elif text == "экономика об-7350-20" or text == "об-7350-20" or text == "об735020":
                send_schedule(7)
                SC_schedule_kb(keyboard)
                send_message(user_id, f"На этом пока все!", keyboard)

            elif text == "информационная безопасность об-7351-20" or text == "об-7351-20" or text == "об735120":
                send_schedule(8)
                SC_schedule_kb(keyboard)
                send_message(user_id, f"На этом пока все!", keyboard)

            # 3 курс #
            elif text == "3 курс":
                send_message(user_id, "Подожди секундочку...")
                TC_schedule_kb(keyboard)
                send_message(user_id, "Смотри, что нашел: \n\n", keyboard)

            elif text == "экономика об-7350-19" or text == "об-7350-19" or text == "об735019":
                send_schedule(11)
                TC_schedule_kb(keyboard)
                send_message(user_id, f"На этом пока все!", keyboard)

            elif text == "информационная безопасность об-7351-19" or text == "об-7351-19" or text == "об735119":
                send_schedule(12)
                TC_schedule_kb(keyboard)
                send_message(user_id, f"На этом пока все!", keyboard)

            # 4 курс #
            elif text == "4 курс":
                send_message(user_id, "Подожди секундочку...")
                FO_schedule_kb(keyboard)
                send_message(user_id, "Смотри, что нашел: \n\n", keyboard)

            elif text == "экономика об-7350-18" or text == "об-7350-18" or text == "об735018":
                send_schedule(15)
                FO_schedule_kb(keyboard)
                send_message(user_id, f"На этом пока все!", keyboard)

            elif text == "информационная безопасность об-7351-18" or text == "об-7351-18" or text == "об735118":
                send_schedule(16)
                FO_schedule_kb(keyboard)
                send_message(user_id, f"На этом пока все!", keyboard)

            ## навигация по кампусу ##
            elif text == "🧭 навигация по ранхигс" or text == "назад к выбору навигации":
                navi_kb(keyboard)
                send_message(user_id, "Что тебя интересует?", keyboard)

            # поиск кабинета #
            elif text == "ищу кабинет":
                navi_kb(keyboard)
                send_message(user_id, serch_kab, keyboard)

            # cхема кампуса #
            elif text == "схема кампуса":
                navi_kb(keyboard)
                send_message(user_id, "Держи схему терретории РАНХиГС:", keyboard)
                navigation.send_kampus(user_id)

            # схема отдельного корпуса #
            elif text == "схема отдельного корпуса":
                sok_kb(keyboard)
                send_message(user_id, "Выбери корпус:", keyboard)

            # схема отдельного корпуса #
            elif '/' in text and len(text) < 7:
                send_message(user_id, "Смотри, что нашел:")
                navigation.send_etaj(text, user_id)

            # схема отдельного корпуса #
            elif "корпус" in text:
                send_message(user_id, "Смотри, что нашел:")
                sok_kb(keyboard)
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

            ## учебные материалы ##
            elif text == "📚 учебные материалы":
                materials_kb(keyboard)
                send_message(
                    user_id, "Ccылка на Яндекс.Диск ПИ: \n\nhttps://disk.yandex.ru/d/X1mkmFS9TpJJiw", keyboard)

            ## полезные ссылки ##
            elif text == "🌐 полезные ссылки":
                link_kb(keyboard)
                send_message(user_id, cool_sites, keyboard)

            ## погода ##
            elif text == "☁ погода":
                main_kb(keyboard)
                send_message(user_id, request.weather_def(), keyboard)

            ## контакты ##
            elif text == "📞 контакты преподавателей":
                main_kb(keyboard)
                send_message(user_id, contacti_pochta, keyboard)

            ## игры ##
            elif text == "🔮 игры":
                game_kb(keyboard)
                send_message(user_id, "Смотри какие игры я знаю:", keyboard)

            ## настройки ##
            elif text == "⚙ настройки":
                set_kb(keyboard)
                send_message(user_id, "Меню настроек", keyboard)

            # идея / сообщить об ошибке #
            elif text == "💡 идея / 🤔 сообщить об ошибке":
                k += 1
                set_kb(keyboard)
                send_message
                send_message(
                    user_id, "Напишите вашу идею или найденную ошибку. Я передам информацию разработчикам, что ты хочем им что-то сообщить", keyboard)

                if dev1_alerts == 1:
                    send_message(dev1_id, f"💡 {user_id}", keyboard)

                if dev2_alerts == 1:
                    send_message(dev2_id, f"💡 {user_id}", keyboard)

            # о боте #
            elif text == "🤖 о боте":
                set_kb(keyboard)
                send_message(user_id, o_bote, keyboard)
            # вопросы / ответы #
            elif text == "❓ f.a.q.":
                set_kb(keyboard)
                send_message(user_id, faq, keyboard)

            # анекдот #
            elif text == "🤡 анекдот":
                send_message(user_id, "Помню я один анекдот, сейчас расскажу...")
                set_kb(keyboard)
                send_message(user_id, request.joke_def(), keyboard)

            ## dev ##
            elif dev1_id == user_id or dev2_id == user_id:

                if text == "dev":
                    dev_kb(keyboard)
                    send_message(user_id, "Здравствуй отец", keyboard)

                elif text == "error":
                    dev_kb(keyboard)
                    send_message(user_id, f"Количество error: {k}", keyboard)

                elif text == "error = 0":
                    k = 0
                    dev_kb(keyboard)
                    send_message(user_id, f"Количество error: {k}", keyboard)

                elif text == "вкл alerts":
                    if dev1_id == user_id:
                        dev1_alerts = 1

                    elif dev2_id == user_id:
                        dev2_alerts = 1

                    send_message(user_id, "alerts вкл")

                elif text == "выкл alerts":
                    if dev1_id == user_id:
                        dev1_alerts = 0

                    elif dev2_id == user_id:
                        dev2_alerts = 0

                    send_message(user_id, "alerts выкл")


# def main_restart():
#     try:
#         main()
#     except Exception as err:
#         print(err)
#         time.sleep(1)
#         main_restart()


# main_restart()

main()