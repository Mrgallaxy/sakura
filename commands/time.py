import datetime
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import sys 

фразы_времени = [
    "сколько времени",
    "какое время сейчас"
]

фразы_даты = [
    "какой сегодня день",
    "какая дата сегодня",
    "какой месяц сейчас",
    "какой год сейчас"
]

def ответить_голосом(текст):
    engine = pyttsx3.init()
    engine.say(текст)
    engine.runAndWait()

def распознать_и_озвучить_время_и_дату():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            распознанный_текст = recognizer.recognize_google(audio, language="ru-RU").lower()

            if any(фраза in распознанный_текст for фраза in фразы_времени):
                текущее_время = datetime.now().strftime("%H:%M")
                ответить_голосом(f"Сейчас {текущее_время}.")
            elif any(фраза in распознанный_текст for фраза in фразы_даты):
                текущая_дата = datetime.now()
                if "какой сегодня день" in распознанный_текст:
                    ответить_голосом(f"Сегодня {текущая_дата.day} число.")
                elif "какая дата сегодня" in распознанный_текст:
                    ответить_голосом(f"Сегодня {текущая_дата.day} {текущая_дата.strftime('%B')}.")
                elif "какой месяц сейчас" in распознанный_текст:
                    ответить_голосом(f"Сейчас {текущая_дата.strftime('%B')}.")
                elif "какой год сейчас" in распознанный_текст:
                    ответить_голосом(f"Сейчас {текущая_дата.year} год.")

        except sr.UnknownValueError:
            print("Не удалось распознать речь.")
        except sr.RequestError as e:
            print(f"Ошибка при подключении к сервису распознавания речи: {e}")
            sys.exit()

распознать_и_озвучить_время_и_дату()