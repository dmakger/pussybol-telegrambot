from utils.ai import GPT


class Gender:
    MALE: str = 'мужчина'
    FEMALE: str = 'девушка'


class People:
    def __init__(self, gender: str = Gender.FEMALE, age: int = 20):
        self.gender = gender
        self.age = age


STYLE_MESSAGE = "Приветик! " \
                "У меня есть отличное предложение для тебя! " \
                "Ищу человека для работы с рекламными панелями. Не сильно сложно, все нюансы и секреты я тебе расскажу и покажу." \
                "Вложения от тебя не нужны, а также не нужны паспортные данные. "


class NLP:
    def __init__(self, people: People):
        self.gpt = GPT()
        self.people = people

    def send(self, text):
        return self.gpt.send(self.get_text(text))

    def get_text(self, text):
        return f"Переформулируй следующий текст и сохраняй пункты:\n" \
               f"{text}\n" \
               f"Допусти от 0 до 2 орфографических ошибок, и сделай его максимально человечным. " \
               f"При этом гендер человека к которому предназначено этот текст не известен. " \
               f"О написавшем: гендер: {self.people.gender}, возраст: {self.people.age}." \
               f"Стиль сообщения: {STYLE_MESSAGE}"
