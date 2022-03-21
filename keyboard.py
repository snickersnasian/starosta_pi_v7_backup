from vk_api.keyboard import VkKeyboardColor

#### цвета для кнопок ####
red = VkKeyboardColor.NEGATIVE
green = VkKeyboardColor.POSITIVE
blue = VkKeyboardColor.PRIMARY
white = VkKeyboardColor.SECONDARY


class _keyboard:
    def start(keyboard):
        keyboard.add_button(label="Начать", color=green)

    #### клавиатура - главное меню ####
    def main_menu(keyboard):
        keyboard.add_button(label="📆 Расписание", color=green)
        keyboard.add_line()

        keyboard.add_button(label="📞 Контакты преподавателей", color=green)
        keyboard.add_line()

        keyboard.add_button(label="🕖 Время работы", color=blue)

        keyboard.add_button(label="🌐 Полезные ссылки", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="🧭 Навигация по РАНХиГС", color=blue)

        keyboard.add_button(label="☁ Погода", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="🔮 Игры", color=blue)

        keyboard.add_button(label="⚙ Настройки", color=white)

    def contacts(keyboard):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="Поиск преподавателя", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Посмотреть весь список", color=blue)

    #### клавиатура - ссылки ####
    def link(keyboard):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_openlink_button(label="📚 Яндекс.Диск 📚", link="https://disk.yandex.ru/d/X1mkmFS9TpJJiw")
        keyboard.add_line()

        keyboard.add_openlink_button(label="🌐 Официальный сайт РАНХиГС", link="http://ranepa.ru")
        keyboard.add_line()

        keyboard.add_openlink_button(label="💼 Личный кабинет", link="http://my.ranepa.ru")

        keyboard.add_openlink_button(label="📖 Кабинет в СДО", link="http://lms.ranepa.ru")
        keyboard.add_line()

        keyboard.add_openlink_button(label="📌 Сайт с расписанием", link="http://lk.ranepa.ru/schedule/")

        keyboard.add_openlink_button(label="📰 Группа в ВК", link="https://vk.com/theacademy")

    #### клавиатура - игры ####
    def games(keyboard):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_vkapps_button(label="2048", app_id=6866893, owner_id=177022076, hash="")
        keyboard.add_line()

        keyboard.add_vkapps_button(label="Джампер", app_id=7590798, owner_id=169484945, hash="")

    #### клавиатура - настройки ####
    def settings(keyboard, x):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="💡 Идея / 🤔 Сообщить об ошибке", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="🤖 О Боте", color=blue)

        keyboard.add_button(label="❓ F.A.Q.", color=blue)
        keyboard.add_line()

        if x == "классический":
            keyboard.add_button(label="Стиль расписания: 📚 Классический", color=blue)
        elif x == "упрощенный":
            keyboard.add_button(label="Стиль расписания: ✂ Упрощенный", color=blue)
        elif x == "без картинок":
            keyboard.add_button(label="Стиль расписания: 🚫 Без картинок", color=blue)

    def style_settings(keyboard, x):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        if x == "классический":

            keyboard.add_button(label="Стиль расписания: 📚 Классический", color=blue)
            keyboard.add_line()

            keyboard.add_button(label="Стиль расписания: ✂ Упрощенный", color=white)
            keyboard.add_line()

            keyboard.add_button(label="Стиль расписания: 🚫 Без картинок", color=white)

        elif x == "упрощенный":
            keyboard.add_button(label="Стиль расписания: 📚 Классический", color=white)
            keyboard.add_line()

            keyboard.add_button(label="Стиль расписания: ✂ Упрощенный", color=blue)
            keyboard.add_line()

            keyboard.add_button(label="Стиль расписания: 🚫 Без картинок", color=white)

        elif x == "без картинок":
            keyboard.add_button(label="Стиль расписания: 📚 Классический", color=white)
            keyboard.add_line()

            keyboard.add_button(label="Стиль расписания: ✂ Упрощенный", color=white)
            keyboard.add_line()

            keyboard.add_button(label="Стиль расписания: 🚫 Без картинок", color=blue)

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

    #### клавиатура - dev ####
    def developer(keyboard):
        keyboard.add_button(label="Главное меню", color=green)
        keyboard.add_line()

        keyboard.add_button(label="Вкл err_mes_user", color=blue)
        keyboard.add_button(label="Выкл err_mes_user", color=blue)

    #### клавиатура - выбор курса ####

    def schedule(keyboard):
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="1 Курс", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="2 Курс", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="3 Курс", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="4 Курс", color=blue)

    #### клавиатура - 1 курс ####
    def FC_schedule(keyboard):
        keyboard.add_button(label="Главное меню", color=green)
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="Экономика ОБ-7350-21", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Цифровые технологии ОБ-230766-21", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Информационная безопасность ОБ-7351-21", color=blue)

    #### клавиатура - 2 курс ####
    def SC_schedule(keyboard):
        keyboard.add_button(label="Главное меню", color=green)
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="Экономика ОБ-7350-20", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Информационная безопасность ОБ-7351-20", color=blue)

    #### клавиатура - 3 курс ####
    def TC_schedule(keyboard):
        keyboard.add_button(label="Главное меню", color=green)
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="Экономика ОБ-7350-19", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Информационная безопасность ОБ-7351-19", color=blue)

    #### клавиатура - 4 курс ####
    def FO_schedule(keyboard):
        keyboard.add_button(label="Главное меню", color=green)
        keyboard.add_button(label="Назад", color=green)
        keyboard.add_line()

        keyboard.add_button(label="Экономика ОБ-7350-18", color=blue)
        keyboard.add_line()

        keyboard.add_button(label="Информационная безопасность ОБ-7351-18", color=blue)
