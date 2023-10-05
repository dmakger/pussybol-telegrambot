from tg.button import Button

START_BUTTON = Button(response="Ладно, отступаю")
BACK_BUTTON = Button(title="Назад", response="Развернулся и алга")

# --------------
#     START
# --------------

# FIRST BUTTONS
ADD_MAMMOTH_BUTTON = Button(title="🦣 Добавить мамонтёнка", response="Выберите как хотите добавить мамонтёнка")
START_MAILING_BUTTON = Button(title="📢 Начать рассылку", response="Рассылка начата")
ADD_SUCCUB_BUTTON = Button(title="👺 Добавить Суккуба",
                           response="Введите API_ID и API_HASH, через пробел или энтер (их можно получить на сайте https://my.telegram.org/apps)")
START_BUTTONS = [
    ADD_MAMMOTH_BUTTON,
    START_MAILING_BUTTON,
    ADD_SUCCUB_BUTTON
]

# ---------------------
#   START/ADD_PEOPLE
# ---------------------

PARSING_BUTTON = Button(title="Поиск по группам", response="Введите группу или группы, разделяя их энтером")
DETAIL_PEOPLE_BUTTON = Button(title="Конкретного мамонтёнка")
TEXT_FILE_BUTTON = Button(title="Текстовый файл")

ADD_PEOPLE_BUTTONS = [
    PARSING_BUTTON,
    DETAIL_PEOPLE_BUTTON,
    TEXT_FILE_BUTTON,
]
