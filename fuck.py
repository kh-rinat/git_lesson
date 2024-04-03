import time

import requests
from bot_config import git_lesson_bot_API

url1 = f"https://api.telegram.org/bot{git_lesson_bot_API}/getMe"
url2 = f"https://api.telegram.org/bot{git_lesson_bot_API}/getUpdates"
url3 = f"https://api.telegram.org/bot{git_lesson_bot_API}/sendMessage?chat_id=680554251&text=idi_nahyi"
url4 = 'https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>&text=AMAZING!'

print(url3)