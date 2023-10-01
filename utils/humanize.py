# Загрузка модели spaCy для русского языка
import spacy

nlp = spacy.load("ru_core_news_sm")


def paraphrase_text(text):
    return str(nlp(text))
