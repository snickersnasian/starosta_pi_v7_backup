from vk_api.keyboard import VkKeyboardColor

#### цвета для кнопок ####
red = VkKeyboardColor.NEGATIVE
green = VkKeyboardColor.POSITIVE
blue = VkKeyboardColor.PRIMARY
white = VkKeyboardColor.SECONDARY


class _keyboard:
    def start(keyboard):
        keyboard.add_button(label="Приступить к работе", color=green)

    #### клавиатура - главное меню ####
    def main_menu(keyboard, profile):
        keyboard.add_button(label="📆 Расписание", color=green)
        keyboard.add_line()

        keyboard.add_button(label="📞 Контакты преподавателей", color=green)
        keyboard.add_line()

        if profile[2] == "4 курс" or profile[2] == "5 курс" or profile[2] == "2 курс Магистратура":
            keyboard.add_button(label="👨‍🎓 Для выпускников", color=green)
            keyboard.add_line()

        keyboard.add_button(label="🧭 Навигация по РАНХиГС", color=blue)

        keyboard.add_button(label="🌐 Полезные ссылки", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="🕖 Часы работы", color=blue)

        keyboard.add_button(label="☁ Погода", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="🔮 Игры", color=blue)

        keyboard.add_button(label="⚙ Настройки", color=white)

    #### генерируем клаву ####
    def gen_schedule(keyboard, name_schedule):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        for i in range(len(name_schedule)):
            keyboard.add_button(label=f"{name_schedule[i-1]}", color=blue)

            if i != (len(name_schedule)-1):
                keyboard.add_line()

    #### клавиатура - ссылки ####
    def link(keyboard):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_openlink_button(
            label="📚 Яндекс.Диск 📚", link="https://disk.yandex.ru/d/X1mkmFS9TpJJiw")
        keyboard.add_line()

        keyboard.add_openlink_button(
            label="📌 Сайт ЭМИТа", link="https://emit.ranepa.ru/faculty-2/ai/")

        keyboard.add_openlink_button(
            label="🌐 Cайт РАНХиГС", link="http://ranepa.ru")
        keyboard.add_line()

        keyboard.add_openlink_button(
            label="💼 Личный кабинет", link="http://my.ranepa.ru")

        keyboard.add_openlink_button(
            label="📖 Кабинет в СДО", link="http://lms.ranepa.ru")
        keyboard.add_line()

        keyboard.add_openlink_button(
            label="📰 Группа в ВК", link="https://vk.com/theacademy")

        keyboard.add_openlink_button(
            label="💭 Психологическая служба", link="https://ion.ranepa.ru/structure/department/psikhologicheskaya-sluzhba/#zapisatsya")

    def contacts(keyboard):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="🔍 Поиск преподавателя", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="📋 Посмотреть весь список", color=blue)

    #### клавиатура - навигация ####
    def navigation(keyboard):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="Ищу кабинет", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Схема кампуса", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Схема отдельного корпуса", color=blue)

    #### клавиатура - Схема отдельного корпуса ####
    def scheme_housing(keyboard):
        keyboard.add_button(label="Главное меню", color=green)
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="Корпус 1", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Корпус 2", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Корпус 3", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Корпус 5", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Корпус 6", color=blue)

    #### клавиатура - игры ####
    def games(keyboard):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_vkapps_button(label="2048", app_id=6866893, owner_id=177022076, hash="")
        keyboard.add_line()

        keyboard.add_vkapps_button(label="Джампер", app_id=7590798, owner_id=169484945, hash="")

    #### клавиатура - dev ####
    def developer(keyboard):
        keyboard.add_button(label="Главное меню", color=green)
        keyboard.add_line()
        
        keyboard.add_button(label="Вкл err_mes_user", color=blue)
        keyboard.add_button(label="Выкл err_mes_user", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Вызвать начальное сообщение", color=blue)

    #### Часы работы ####
    def work_time(keyboard): 
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="💼 Деканат", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="🍕 Точки питания", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="🚑 Медицинский центр РАНХиГС", color=blue)


    #### клавиатура - настройки ####
    def settings(keyboard):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="💡 Идея / 🤔 Сообщить об ошибке", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="🤖 О Боте", color=blue)

        keyboard.add_button(label="❓ F.A.Q.", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="📋 Настройки профиля", color=blue)

    #### генерируем клаву для настроек профиля ####
    def gen_profile_set(keyboard, set):
        for i in range(len(set)):
            keyboard.add_button(label=f"{set[i-1]}", color=blue)

            if (i != (len(set)-1)) and (len(set)-1 % 2 == 0):
                keyboard.add_line()

    def profile(keyboard, profile):
        style = profile[5]

        if style == "классический":
            slyle_kb = "Стиль расписания: 📚 Классический"
        elif style == "упрощенный":
            slyle_kb = "Стиль расписания: ✂ Упрощенный"
        elif style == "без картинок":
            slyle_kb = "Стиль расписания: 🚫 Без картинок"

        keyboard.add_button(label="Главное меню", color=green)
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label=f"Курс: {profile[2]}", color=blue)
        keyboard.add_line()

        keyboard.add_button(label=f"Форма обучения: {profile[3]}", color=blue)
        keyboard.add_line()

        keyboard.add_button(label=slyle_kb, color=blue)

    def style_settings(keyboard, x):
        keyboard.add_button(label="Главное меню", color=green)

        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        if x == "классический":

            keyboard.add_button(
                label="Стиль расписания: 📚 Классический", color=blue)
            keyboard.add_line()

            keyboard.add_button(
                label="Стиль расписания: ✂ Упрощенный", color=white)
            keyboard.add_line()

            keyboard.add_button(
                label="Стиль расписания: 🚫 Без картинок", color=white)

        elif x == "упрощенный":
            keyboard.add_button(
                label="Стиль расписания: 📚 Классический", color=white)
            keyboard.add_line()

            keyboard.add_button(
                label="Стиль расписания: ✂ Упрощенный", color=blue)
            keyboard.add_line()

            keyboard.add_button(
                label="Стиль расписания: 🚫 Без картинок", color=white)

        elif x == "без картинок":
            keyboard.add_button(
                label="Стиль расписания: 📚 Классический", color=white)
            keyboard.add_line()

            keyboard.add_button(
                label="Стиль расписания: ✂ Упрощенный", color=white)
            keyboard.add_line()

            keyboard.add_button(
                label="Стиль расписания: 🚫 Без картинок", color=blue)

    #### клавиатура - выбор курса ####
    def course(keyboard, profile):
        if profile[2] != "не указан":
            keyboard.add_button(label="Назад", color=green)
            keyboard.add_line()

        keyboard.add_button(label="1 курс", color=blue)

        keyboard.add_button(label="2 курс", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="3 курс", color=blue)

        keyboard.add_button(label="4 курс", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="5 курс", color=blue)

        # keyboard.add_button(label="&#4448;", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="1 курс Магистратура", color=blue)

        keyboard.add_button(label="2 курс Магистратура", color=blue)

    def forma(keyboard, profile):
        if profile[3] != "не указан":
            keyboard.add_button(label="Назад", color=green)
            keyboard.add_line()

        keyboard.add_button(label="Очная форма", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Очно-заочная форма", color=blue)

    def vipusk(keyboard):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="👥 Научное руководство/Консультанты", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="📈 График предзащит и защит", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="📚 Электронная библиотека РАНХиГС", color=blue)

    def test(keyboard):
        keyboard.add_button(label="Главное меню", color=green)

        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="test1", color=green)
        keyboard.add_line()

        keyboard.add_button(label="test1", color=green)

    def naychnik(keyboard, google_sheets):
        keyboard.add_button(label="Главное меню", color=green)

        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        google_sheets_new = []

        for i in range(len(google_sheets)):
            if (google_sheets[i][1] > 0 and google_sheets[i][1] < 15):
                google_sheets_new.append(google_sheets[i])

        for i in range(len(google_sheets_new)):

            if (i != (len(google_sheets_new)-1) and ((i-1) % 2) == 0):
                keyboard.add_button(label=f"{google_sheets_new[i][0]}", color=blue)
                keyboard.add_line()
            else:
                keyboard.add_button(label=f"{google_sheets_new[i][0]}", color=blue)




