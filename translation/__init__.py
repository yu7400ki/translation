from transformers import pipeline

ej_translator = pipeline("translation", model="staka/fugumt-en-ja")
ja_translator = pipeline("translation", model="staka/fugumt-ja-en")


def translate_en(text: str) -> str:
    return ej_translator(text)[0]["translation_text"]


def translate_ja(text: str) -> str:
    return ja_translator(text)[0]["translation_text"]
