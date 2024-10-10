from config import *

ADMIN_ID = [6280414588, 6644161333]
token = "6470372626:AAGto8aFByraUzop3fml_JiqSvnOmMCIhbk"

def check_screen_size() -> list:
    value_str = config.get("Friday", "screen_size")
    values = value_str.strip("[]").split(",")

    width = int(values[0].strip())
    height = int(values[1].strip())

    if width < 400:
        width = 400
    if width > 2999:
        width = 2999
    
    if height < 400:
        height = 400
    if height > 2999:
        height = 2999

    return width, height