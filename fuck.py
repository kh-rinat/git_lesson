import time

import requests
from bot_config import git_lesson_bot_API

url1 = f"https://api.telegram.org/bot{git_lesson_bot_API}/getMe"
url2 = f"https://api.telegram.org/bot{git_lesson_bot_API}/getUpdates"
url3 = f"https://api.telegram.org/bot{git_lesson_bot_API}/sendMessage?chat_id=680554251&text=idi_nahyi"




def take_data(url):
    response = requests.get(url).json()
    print(response)


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = git_lesson_bot_API
TEXT = 'Ура! Классный апдейт!'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1
