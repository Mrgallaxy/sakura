import os
from PIL import ImageGrab
from plyer import notification

# Получаем путь к рабочему столу пользователя
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Делаем скриншот всего экрана
screenshot = ImageGrab.grab()

# Путь для сохранения скриншота на рабочем столе
save_path = os.path.join(desktop_path, "sakura.png")

# Сохраняем скриншот
screenshot.save(save_path)

# Текст уведомления
title = 'Уведомление'
message = 'Ваш скриншот успешно сохранен на рабочем столе!'

# Отправка уведомления
notification.notify(title=title, message=message)

