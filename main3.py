from utils.nlp import People, NLP

TEXT = "❗️ доброе время суток , у меня имеется для вас предложение." \
       "Я ищу человека для работы. нужно работать с рекламными панелями . работа не сложная." \
       "🔵я всему обучу и расскажу все нюансы работы" \
       "🔵от вас вложения не нужны" \
       "🔵Паспортные данные не требуются"


def main():
    people = People()
    nlp = NLP(people)
    for num in range(10):
        print(nlp.send(TEXT))
        print('----------------')


if __name__ == '__main__':
    main()
