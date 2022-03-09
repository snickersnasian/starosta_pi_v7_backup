from vk_api.keyboard import VkKeyboardColor

#### цвета для кнопок ####
red = VkKeyboardColor.NEGATIVE
green = VkKeyboardColor.POSITIVE
blue = VkKeyboardColor.PRIMARY
white = VkKeyboardColor.SECONDARY

#### клавиатура - главное меню ####
def main_kb(keyboard):
    keyboard.add_button(label="📆 Расписание", color=green)
    keyboard.add_line()

    keyboard.add_button(label="📚 Учебные материалы", color=green)
    keyboard.add_line()

    keyboard.add_button(label="📞 Контакты преподавателей", color=blue)

    keyboard.add_button(label="🌐 Полезные ссылки", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="🧭 Навигация по РАНХиГС", color=blue)

    keyboard.add_button(label="☁ Погода", color=blue)
    keyboard.add_line()
    
    keyboard.add_button(label="🔮 Игры", color=blue)

    keyboard.add_button(label="⚙ Настройки", color=white)

#### клавиатура - материалы ####
def materials_kb(keyboard):
    keyboard.add_button(label="Назад", color=green)
    keyboard.add_line()

    keyboard.add_openlink_button(label="📚 Яндекс.Диск 📚", link="https://disk.yandex.ru/d/X1mkmFS9TpJJiw")

#### клавиатура - ссылки ####
def link_kb(keyboard):
    keyboard.add_button(label="Назад", color=green)
    keyboard.add_line()

    keyboard.add_openlink_button(label="🌐 Официальный сайт РАНХиГС", link="http://ranepa.ru")
    keyboard.add_line()

    keyboard.add_openlink_button(label="💼 Личный кабинет", link="http://my.ranepa.ru")

    keyboard.add_openlink_button(label="📖 Кабинет в СДО", link="http://lms.ranepa.ru")
    keyboard.add_line()

    keyboard.add_openlink_button(label="📌 Сайт с расписанием", link="http://lk.ranepa.ru/schedule/")

    keyboard.add_openlink_button(label="📰 Группа в ВК", link="https://vk.com/theacademy")

#### клавиатура - игры ####
def game_kb(keyboard):
    keyboard.add_button(label="Назад", color=green)
    keyboard.add_line()

    keyboard.add_vkapps_button(label="2048", app_id=6866893, owner_id=177022076, hash="")
    keyboard.add_line()

    keyboard.add_vkapps_button(label="Джампер", app_id=7590798, owner_id=169484945, hash="")

#### клавиатура - настройки ####
def set_kb(keyboard):
    keyboard.add_button(label="Назад", color=green)
    keyboard.add_line()

    keyboard.add_button(label="💡 Идея / 🤔 Сообщить об ошибке", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="🤖 О Боте", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="❓ F.A.Q.", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="🤡 Анекдот", color=blue)

#### клавиатура - навигация ####
def navi_kb(keyboard):
    keyboard.add_button(label="Назад", color=green)
    keyboard.add_line()

    keyboard.add_button(label="Ищу кабинет", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="Схема кампуса", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="Схема отдельного корпуса", color=blue)

#### клавиатура - Схема отдельного корпуса ####
def sok_kb(keyboard):
    keyboard.add_button(label="Назад в Главное меню", color=green)
    keyboard.add_button(label="Назад к Выбору Навигации", color=green)
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
def dev_kb(keyboard):
    keyboard.add_button(label="Назад", color=green)
    keyboard.add_line()

    keyboard.add_button(label="error", color=blue)
    keyboard.add_line()
    
    keyboard.add_button(label="error = 0", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="Вкл alerts", color=blue)
    keyboard.add_button(label="Выкл alerts", color=blue)

#### клавиатура - выбор курса ####
def schedule_kb(keyboard):
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
def FC_schedule_kb(keyboard):
    keyboard.add_button(label="Назад в Главное меню", color=green)
    keyboard.add_button(label="Назад к Выбору курса", color=green)
    keyboard.add_line()

    keyboard.add_button(label="Экономика ОБ-7350-21", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="Цифровые технологии ОБ-230766-21", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="Информационная безопасность ОБ-7351-21", color=blue)

#### клавиатура - 2 курс ####
def SC_schedule_kb(keyboard):
    keyboard.add_button(label="Назад в Главное меню", color=green)
    keyboard.add_button(label="Назад к Выбору курса", color=green)
    keyboard.add_line()

    keyboard.add_button(label="Экономика ОБ-7350-20", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="Информационная безопасность ОБ-7351-20", color=blue)

#### клавиатура - 3 курс ####
def TC_schedule_kb(keyboard):
    keyboard.add_button(label="Назад в Главное меню", color=green)
    keyboard.add_button(label="Назад к Выбору курса", color=green)
    keyboard.add_line()

    keyboard.add_button(label="Экономика ОБ-7350-19", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="Информационная безопасность ОБ-7351-19", color=blue)

#### клавиатура - 4 курс ####
def FO_schedule_kb(keyboard):
    keyboard.add_button(label="Назад в Главное меню", color=green)
    keyboard.add_button(label="Назад к Выбору курса", color=green)
    keyboard.add_line()

    keyboard.add_button(label="Экономика ОБ-7350-18", color=blue)
    keyboard.add_line()

    keyboard.add_button(label="Информационная безопасность ОБ-7351-18", color=blue)