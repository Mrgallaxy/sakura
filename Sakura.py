#  ____      _     _  __ _   _  ____      _
# / ___|    / \   | |/ /| | | ||  _ \    / \
# \___ \   / _ \  | ' / | | | || |_) |  / _ \
#  ___) | / ___ \ | . \ | |_| ||  _ <  / ___ \
# |____/ /_/   \_\|_|\_\ \___/ |_| \_\/_/   \_\


#библиотеки
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
# import speech_recognition as sr #Распозвнование речи
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

global window
global exit_
global maximi

global started

started = False



exit_ = False
maximi = False

name = "Sakura"
developers = "TheYoledayYT & ShadowDarkness"
links = [
    "https://www.youtube.com/channel/UCVEGSAvkcIPhoCzcNPlQqFw",
    "https://www.donationalerts.com/r/theyoledayyt"
]



def say(text: str, file:str) -> None:
    add_assistant_text(text)
    playsound.playsound(file)

def minimize():
    global window

    window.minimize()

def maximize():
    global window
    global maximi

    if maximi == False:
        window.maximize()
        maximi = True
    else:
        window.restore()
        maximi = False

def close():
    global window
    global exit_

    exit_ = True
    window.destroy()

def save_chat_history(history):
    with open("temp/chat_history.txt", "w", encoding="utf-8") as file:
        file.write(history)

def clear_chat_history(file_path:str="./temp/chat_history.txt"):
    global window

    with open(file_path, "w") as file:
        pass
    file.close()

    window.evaluate_js("loadHistoryFromFile();")

def load_html(html):
    global window

    window.load_url(html)

def add_assistant_text(message:str):
    global window

    window.evaluate_js("add_assistant_message('{}');".format(message))

def add_people_text(message:str):
    if message == "":
        return
    
    global window

    window.evaluate_js("add_people_message('{}');".format(message))

def save_screen_size(width, height):
    global window

    # config["Phoenix"]["screen_size"] = [f"{width}", f"{height}"]
    config.set("Sakura", "screen_size", str([width, height]))
    save_ini_file(config)

    window.resize(width=width, height=height)

def Sakura():
    global window

    w, h = check_screen_size()
    
    window = webview.create_window("Sakura", url="index.html",
        width=w, height=h, frameless=True, easy_drag=False, resizable=True)
    window.expose(minimize, maximize, close, save_chat_history, load_html, save_screen_size)
    webview.start(debug=False, func=vosk_)

def command(text):
    def set_volume_(volume):
        sleep(0.2)
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        volume_interface.SetMasterVolumeLevelScalar(volume, None)

    def extract_number_from_text(text):
        words = text.split()
        result = 0
        print(words)
        for word in words:
            print(word)
            if word in numbers:
                result += int(numbers[word])

        return result

    def extract_buttons(text):
        words = text.split()
        result = ""
        print(words)
        for word in words:
            print(word)
            if word == buttons:
                result += f"{buttons[word]}+"

        return result

    def randomazie_sait() -> None:
        max_audio = 4
        audio_s = {
            "./sait/gotovo.wav": "Готово",
            "./sait/opennew.wav": "Открыла",
            "./sait/vupolnila.wav": "Выполнила",
            "./sait/zapusk.wav": "Запуск"
        }

        random_ = randint(1, max_audio)

        if random_ == 1:
            audio = "./sait/gotovo.wav"
            text = audio_s[audio]

        elif random_ == 2:
            audio = "./sait/opennew.wav"
            text = audio_s[audio]

        elif random_ == 3:
            audio = "./sait/vupolnila.wav"
            text = audio_s[audio]

        elif random_ == 4:
            audio = "./sait/zapusk.wav"
            text = audio_s[audio]

        print(audio, text)

        say(text, audio)

    enter_text = ("напиши", "пиши", "введи", "в веди", "напиши на экране")
    set_volume = ["поставь громкость на", "установи громкость на", "измени громкость на", "громкость", "громкость на"]
    hello = ["привет", "сакура", "добрый день", "доброе утро", "добрый вечер"]
    closed = ["закрой окно", "закрой", "выйди"]
    command = ["покажи команды", "лист команд", "команды", "какие есть команды"]
    youtube = ["ютуб", "открой ютуб", "запусти ютуб"]
    vk = ["века", "открой века", "запусти века"]
    kinopoisk = ["кинопоиск","открой кинопоиск"]
    yandex = ["яндекс", "открой яндекс", "запусти яндекс"]
    gmail = ["гугл почта", "открой гугл почту", "запусти гугл почту"]
    yandexmail = ["яндекс почта", "открой яндекс почту", "запусти яндекс почту"]
    channelSakura = ["канал сакуры", "открой канал сакура", "запусти канал сакура"]
    cntlv = ["вставь", "вставь текст", "вставь изоображение"]
    cntrlc = ["скопировать", "скопировать текст", "скопировать изооражение", ]
    vozrattab = ["верни вкладку","открой закрытую вкладку"]
    closetabbrowser = ["закрой вкладку", "выйди из вкладки"]
    languagechange = ["смени язык", "поставь другой язык"]
    yandexmusic = ["яндекс музыка", "запусти яндекс музыку", "открой яндекс музыку"]
    spotify = ["спотифай", "запусти спотифай", "открой спотифай"]
    history = ["очисти историю", "история", "перезапути историю"]
    up =  ["листни вверх","вверх","скрол вверх"]
    down =  ["листни вниз","вниз","скрол вниз"]
    lkm = ["нажми левой кнопкой", "левая кнопка мыши", "левая кнопка"]
    pkm = ["нажми правой кнопкой", "правая кнопка мыши", "правая кнопка"]
    shutdown =  ["выключи пк", "выключение пк", "убей пк"]
    sleepmode = ["спящий режим","включи спящий режим"]
    restart = ["перезагрузка","перезагрузи пк"]
    screenshot = ["скриншот", "сделай скриншот"]
    textall = ["выдели весь текст", "выдели текст"]
    offvolume = ["без звука", "убери звук", "режим космос"]
    newtab = ["новая вкладка", "создай вкладку"]
    favoritetab = ["сохрани вкладку", "поставь вкладку в избранное"]
    clearbrowserhistory = ["отчисти историю", "скрой историю"]
    reloadsait = ["перезапусти сайт", "перезагрузи сайт"]
    downloadfiles = ["загрузки", "открой загрузки", "загрузки браузера"]
    svertwindow = ["сверни","сверни окно"]
    svertwindows = ["сверни всё","сверни окна"]
    windowselect = ["другое окно", "выбери другое окно"]
    razwindow  = ["разверни", "разверни окно"]
    razwindows = ["разверни всё", "разверни окна"]
    korzina = ["перемести файл в корзину", "файл в корзину"]
    deleteall = ["удали файл", "удали файл полностью"]
    searchgoogle = ["найди", "найди в интернере"]

    stop_media = ["останови видео", "останови музыку", "поставь на паузу видео", "поставь на паузу музыку", "пауза", "сними с паузы", "убери паузу", "поставь на паузу"]
    next_track = ["следующий трек", "следующая песня"]
    prev_track = ["предыдущий трек", "предыдущая песня"]
    



    for i in hello:
        if i == text:
            say("Здравствуйте, хозяин!", '.golos/welcomeforacode.wav')
    
    if 'как дела?' == text:
        say("Всегда хорошо", 'golos/gooddela.wav')
    
    if 'скриншот области' == text:
        keyboard.press_and_release('Win+Shift+S')
        say("Сделала скриншот области", 'golos/make a screenshot.wav')

    if 'открой проводник' == text:
        keyboard.press_and_release('Win+E')
        say("Открыла проводник", 'golos/open a explorer.wav')
        
    if 'создай папку'== text:
        os.system(f'python foldersakura.py')
        say("Готово", 'golos/good.wav')

    if 'лучшая песня' == text:
        webbrowser.open_new('https://www.youtube.com/watch?v=M6hG0JLlrY8')    
    
    if 'протокол уютный вечер' == text:
        say("Протокол уютный вечер готов", 'golos/yutnuivechergotov.wav')
        os.system(f'python yutnuivechergotov.py')

    if 'отправь сообщение' == text:
        say("Отправила", 'golos/send.wav')
        keyboard.press_and_release("Enter")

    for i in svertwindow:
        if i == text:
            pyautogui.hotkey('winleft', 'down')

    for i in svertwindows:
        if i == text:
            pyautogui.hotkey('win', 'd')

    for i in windowselect:
        if i == text:
            keyboard.press_and_release("Alt+Tab")

    for i in searchgoogle:
        if i in text:
            say("Скажите что нужно найти", 'golos/searchgoogle.wav')
            os.system(f'python google-speak-search1.py')
            

    for i in razwindow:
        if i == text:
            pyautogui.hotkey('winleft', 'up')

    for i in razwindows:
        if i == text:
            pyautogui.hotkey('win', 'd')

    for i in up:
        if i == text:
            mouse.wheel(10)

    for i in down:
        if i == text:
            mouse.wheel(-10)

    for i in lkm:
        if i == text:
            mouse.click("left")

    for i in textall:
        if i == text:
            keyboard.press_and_release("Ctrl+A")

    for i  in pkm:
        if i == text:
            mouse.click("right")

    for i in screenshot:
        if i == text:
            os.system(f'python screenshot.py')
            say("Скриншот сделан", 'golos/screenshot.wav')


    for i in youtube:
        if i == text:
            randomazie_sait()
            webbrowser.open_new('https://www.youtube.com')

    for i in vk:
        if i == text:
            randomazie_sait()
            webbrowser.open_new('https://vk.com')

    for i in yandex:
        if i == text:
            randomazie_sait()
            webbrowser.open_new('https://yandex.kz/')

    for i in gmail:
        if i == text:
            randomazie_sait()
            webbrowser.open_new('https://mail.google.com/mail/u/0/#inbox')

    for i in yandexmail:
        if i == text:
            randomazie_sait()
            webbrowser.open_new('https://mail.yandex.ru/#inbox')

    for i in channelSakura:
        if i == text:
            randomazie_sait()
            webbrowser.open_new('https://www.youtube.com/channel/UC04YhLcxChiAb4oW3Emyx0A')

    for i in kinopoisk:
        if i == text:
            randomazie_sait()
            webbrowser.open_new('https://www.kinopoisk.ru/')

    for i in newtab:
        if i == text:
            keyboard.press_and_release("Ctrl+T")
            randomazie_sait

    for i in shutdown:
        if i == text:
            say("Выключаю", 'golos/shutdown.mp3')
            keyboard.press_and_release('Win+R')
            sleep(2)
            keyboard.write(text="shutdown /s /t 0", delay=0.05)
            keyboard.press_and_release("Enter")

    for i in favoritetab:
        if i == text:
            keyboard.press_and_release("Ctrl+D")
            say("Сохранила", 'golos/save.wav')

    for i in reloadsait:
        if i == text:
            keyboard.press_and_release("F5")
            say("Выполнила", 'sait/vupolnila.wav')

    for i in clearbrowserhistory:
        if i == text:
            keyboard.press_and_release("Ctrl+Shift+Del")
            say("Отчистила", 'golos/clearhistory.wav')

    for i in downloadfiles:
        if i == text:
            keyboard.press_and_release('Ctrl+J')
            randomazie_sait()

    for i in korzina:
        if i == text:
            keyboard.press_and_release('Del')

    for i in deleteall:
        if i == text:
            keyboard.press_and_release('Shift+Del')
            sleep(1)
            keyboard.press_and_release('Enter')

    for i in restart:
        if i == text:
            say("Перезагружаю", 'golos/restart.wav')
            keyboard.press_and_release('Win+R')
            sleep(2)
            keyboard.write(text="shutdown /r /t 0", delay=0.05)
            keyboard.press_and_release("Enter")

    for i in sleepmode:
        if i == text:
            say("Cпящий режим актвирован", 'golos/sleepmode.wav')
            keyboard.press_and_release('Win+R')
            sleep(2)
            keyboard.write(text="shutdown /h", delay=0.05)
            keyboard.press_and_release("Enter")


    for i in closed:
        if i == text:
            say("Закрыла", 'golos/closed.wav')
            keyboard.press('Alt')
            keyboard.press('F4')
            keyboard.release('Alt')
            keyboard.release('F4')

    for i in yandexmusic:
        if i == text:
            randomazie_sait
            webbrowser.open_new('https://music.yandex.ru/home')

    for i in spotify:
        if i == text:
            randomazie_sait()
            webbrowser.open_new('https://open.spotify.com/')

    for i in closetabbrowser:
        if i == text:
            keyboard.press_and_release("Ctrl+W")
            say("Вкладка закрыта", '.go/golos/closetabbrowser.wav')

    for i in vozrattab:
        if i == text:
            keyboard.press_and_release('Ctrl+Shift+T')
            say("Вернула вкладку", 'golos/vozvratbrowser.wav')

    for i in cntrlc:
        if i == text:
            keyboard.press_and_release('ctrl+c')
            say("Скопировала", 'golos/ctrlc.wav')



    if 'телеграмм бот' == text:
        say("Выполнила", 'golos/sait.wav')
        os.system(f'python tgbot.py')

    if 'протокол стрим' ==  text:
        os.system(f'python stream.py')
        say("Протокол стрим загружен", './golos/stream.py')

    if 'канал создателя' == text:
        say("Выполнила", 'golos/sait.wav')
        webbrowser.open_new('https://www.youtube.com/channel/UCVEGSAvkcIPhoCzcNPlQqFw')

    if 'увеличить яркость' == text:
        change_brightness(10)

    if 'уменьши яркость' == text:
        change_brightness(-10)

    if 'помощь' == text:
        say("Выполнила", 'golos/sait.wav')
        webbrowser.open_new('https://t.me/Sakurasupportbot') 

    for i in cntlv:
        if i == text:
            keyboard.press_and_release('ctrl+v')
            say("Вставила", './sait/ctrlv.wav')      
    
    for i in history:
        clear_chat_history()

    for i in command:
        if i == text:
            say("Вот все команды", 'golos/commands.wav')
            os.system(f'python listcommands.py')

    for i in stop_media:
        if i in text:
            pyautogui.press("playpause")

    for i in next_track:
        if i in text:
            pyautogui.press("nexttrack")
          
    for i in prev_track:
        if i in text:
            pyautogui.press("prevtrack")

    for i in enter_text:
        words = text.split()
        if i in words:
            text_ = text.replace(f"{i} ", "")
            keyboard.write(text=text_, delay=0.05)
            return
        
    for i in set_volume:
        if i in text:
            text = text.replace(f"{i} ", "")
            volume = extract_number_from_text(text)

            if volume == 100:
                volume = 1
            elif volume == 0:
                volume = 0

            elif volume == 1:
                volume = 0.01
                
            elif volume == 2:
                volume = 0.02
                
            elif volume == 3:
                volume = 0.03
                
            elif volume == 4:
                volume = 0.04
                
            elif volume == 5:
                volume = 0.05
                
            elif volume == 6:
                volume = 0.06
                
            elif volume == 7:
                volume = 0.07
                
            elif volume == 8:
                volume = 0.08
                
            elif volume == 9:
                volume = 0.09
            else:
                volume = float(f"0.{volume}")
            
            set_volume_(volume)

    for i in languagechange:
        if i == text:
            keyboard.press_and_release("Win+Space")
            say("Сменила", 'golos/languagechange.wav')

    for i in offvolume:
        if i == text:
            mute_volume()
    
    for i in press_words:
        if i in text:
            key = text.replace(f"{i} ", "")
            key = extract_buttons(key)

            if key[-1] == "+":
                key = key[:-1]

            keyboard.press_and_release(key)

    for i in pressing_words:
        if i in text:
            key = text.replace(f"{i} ", "")
            key = extract_buttons(key)

            if key[-1] == "+":
                key = key[:-1]

            keyboard.press(key)

    for i in unpressing_words:
        if i in text:
            key = text.replace(f"{i} ", "")
            key = extract_buttons(key)
            
            if key[-1] == "+":
                key = key[:-1]

            keyboard.release(key)

    if 'выход' == text:
        say("Удачи", 'golos/udachi.wav')
        clear_chat_history()
        close()

#ютуб

# def listen():
#     try:
#         r = sr.Recognizer()

#         with sr.Microphone() as source:
#             print('Слушаю...')
#             r.pause_threshold = 1
#             audio = r.listen(source, timeout=4, phrase_time_limit=4)

#         text = r.recognize_google(audio, language="ru-RU").lower()
#         print(text)
#         return text.replace('ё', 'е')
#     except sr.UnknownValueError:
#         return ''
#     except sr.WaitTimeoutError:
#         return ''



def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')  # Используем женский голос на macOS
    engine.say(text)
    engine.runAndWait()

def get_time():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    if hour == 0:
        hour = 12
    elif hour > 12:
        hour -= 12
    time_str = f"{hour} часов {minute} минут"
    return time_str
 
def change_brightness(delta):
    # Здесь должна быть логика изменения яркости, например, с использованием библиотеки, управляющей экраном
    pass

# Получаем путь к рабочему столу
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Имя базовой папки
base_folder_name = 'Sakura'

# Функция для создания новой папки с уникальным именем
def create_unique_folder(base_path, base_name):
    counter = 1
    while True:
        new_folder_name = f"{base_name}{counter}"
        new_folder_path = os.path.join(base_path, new_folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            return new_folder_path
        counter += 1

# Проверяем существует ли папка "Sakura" на рабочем столе


def mute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-100.0, None)  


def vosk_():
    def find_input_device_index():
        input_device_index = p.get_default_input_device_info()["index"]

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

    stream = p.open(format=FORMAT,
                    channels=1,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=FRAMES_PER_BUFFER,
                    input_device_index=input_device_index)

    global started


    while exit_ != True:
        try:
            data = stream.read(FRAMES_PER_BUFFER, exception_on_overflow=False)
            audio_level = max(abs(sample) for sample in data)


            if audio_level > THRESHOLD:
                if recognizer.AcceptWaveform(data):
                    result = recognizer.Result()
                    print(result[14:-3])
                    add_people_text(result[14:-3])
                    command(str(result[14:-3]).lower())




        except Exception as e:
            print(f"Ошибка: {e}")

def start():
    Sakura()

if __name__ == "__main__":
    start()



