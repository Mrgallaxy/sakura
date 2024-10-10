import webview
import webbrowser
import keyboard # Управление клавиатурой
import os # Управление системой
import sys # Управление системой
import mouse # Управление мышкой
import pyaudio #Распознание микрофона
import playsound #Проигрывает слова
import pyautogui
import pyttsx3
import datetime
import threading
import pystray, PIL.Image
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from screen_brightness_control import get_brightness 
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pathlib import Path




from config import *
from load_checker import *

from time import sleep

from random import randint

from time import sleep
from vosk import Model, KaldiRecognizer


def vosk_():
    def find_input_device_index():
        input_device_index = p.get_default_input_device_info()["index"]

        try:
            print("Распознавание...")
            query = recognizer.recognize_google(vosk_, language='ru-RU')
            pass
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
        except:
            pass

        if input_device_index > 0:
            return input_device_index
        else:
            return None
        


    global exit_

    FORMAT = pyaudio.paInt16
    RATE = 16000
    FRAMES_PER_BUFFER = 2000
    THRESHOLD = 200

    p = pyaudio.PyAudio()

    vosk_model = Model("./ru-model")

    recognizer = KaldiRecognizer(vosk_model, RATE)

    input_device_index = find_input_device_index()

    if input_device_index is None:
        print("Ошибка: Микрофон не найден.")
        sys.exit()
    else:
        print(f"Выбран микрофон (индекс): {input_device_index}")

vosk_()
