import os
from PIL import ImageGrab
from plyer import notification

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

screenshot = ImageGrab.grab()

save_path = os.path.join(desktop_path, "sakura.png")

screenshot.save(save_path)

title = 'Уведомление'
message = 'Ваш скриншот успешно сохранен на рабочем столе!'

notification.notify(title=title, message=message)

