import speech_recognition as sr
import pyttsx3
import webbrowser
import sys
import winreg

def speak(текст):
    engine = pyttsx3.init()
    engine.say(текст)
    engine.runAndWait()

def get_default_browser():
    # Для Windows
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice")
        browser = winreg.QueryValueEx(key, "ProgId")[0]

        if "chrome" in browser.lower():
            return "chrome"
        elif "firefox" in browser.lower():
            return "firefox"
        elif "edge" in browser.lower():
            return "edge"
        elif "opera" in browser.lower():
            return "opera"
        elif "yandex" in browser.lower():
            return "yandex"
        elif "tor" in browser.lower():
            return "tor"
        elif "operagx" in browser.lower():
            return "opera_gx"
        else:
            return "default"
    except Exception as e:
        print(f"Ошибка при получении браузера по умолчанию: {e}")
        return "default"

def browser_search():
    ключевые_фразы = [
        "поиск в браузере",
        "найди в браузере",
        "найди в интернете"
    ]

    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    default_browser = get_default_browser()

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            распознанный_текст = recognizer.recognize_google(audio, language="ru-RU").lower()

            if any(фраза in распознанный_текст for фраза in ключевые_фразы):
                запрос = распознанный_текст.replace("поиск в браузере", "").replace("найди в интернете", "").replace("найди в браузере", "").strip()
                if запрос:
                    speak(f"Ищу {запрос} в Google.")
                    search_url = f"https://www.google.com/search?q={запрос}"

                    if default_browser == "chrome":
                        webbrowser.get("chrome").open(search_url)
                    elif default_browser == "firefox":
                        webbrowser.get("firefox").open(search_url)
                    elif default_browser == "edge":
                        webbrowser.get("edge").open(search_url)
                    elif default_browser == "opera":
                        webbrowser.get("opera").open(search_url)
                    elif default_browser == "yandex":
                        webbrowser.get("yandex").open(search_url)
                    elif default_browser == "tor":
                        webbrowser.get("tor").open(search_url)
                    elif default_browser == "opera_gx":
                        webbrowser.get("opera_gx").open(search_url)
                    else:
                        webbrowser.open(search_url)

        except sr.UnknownValueError:
            print("Не удалось распознать речь.")
        except sr.RequestError as e:
            print(f"Ошибка при подключении к сервису распознавания речи: {e}")
            sys.exit()

browser_search()
