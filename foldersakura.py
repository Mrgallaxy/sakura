
from plyer import notification
import os

# Получаем путь к рабочему столу
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

def create_unique_folder(base_path, base_name):
    counter = 1
    while True:
        new_folder_name = f"{base_name}{counter}"
        new_folder_path = os.path.join(base_path, new_folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            return new_folder_path
        counter += 1

# Имя базовой папки
base_folder_name = 'Sakura'
sakura_path = os.path.join(desktop_path, base_folder_name)
if not os.path.exists(sakura_path):
    os.makedirs(sakura_path)
else:
    new_folder_path = create_unique_folder(desktop_path, base_folder_name)
    # Текст уведомления
    title = 'Папка'
    message = 'Ваша папка успешно создана!'

    # Отправка уведомления
    notification.notify(title=title, message=message)