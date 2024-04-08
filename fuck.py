import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from bot_config import git_lesson_bot_API

BOT_TOKEN = git_lesson_bot_API

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

ATTEMPS = 5

user = {'in_game': False,
        'secret_number': None,
        'attemps': None,
        'total_games': 0,
        'wins': 0
}

def get_random():
    return random.randint(a=1, b=100)

@dp.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text="HI, bro!\nLets play the game\nsend help commant for rools watchig")

@dp.message(Command(commands='help'))
async def process_command_help(message: Message):
    await message.answer(text=f"You have {ATTEMPS} attemps for predict random number\navailable comands:\n/cansell - stop the game\n/stat - watch your stat")

@dp.message(Command(commands='stat'))
async def process_command_stat(message: Message):
    await message.answer(text=f"total count of games - {user['total_games']}\ncount of wins - {user['wins']}")

@dp.message(Command(commands='cansell'))
async def process_command_stat(message: Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer(text="you canselled the game!\nWelcome to play any time")
    else:
        await message.answer(text="FUCK YOU! You are not in game at this moment")

@dp.message(F.text.lower().in_(['yes', 'lets play', 'begin', 'game', 'want to play']))
async def process_positive_answer(message: Message):
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = get_random()
        user['attemps'] = ATTEMPS
        await message.answer(f"Start your prediction")
    else:
        await message.answer("You are in game now, firstly finish current game or cansell currnet game")

@dp.message(F.text.lower().in_(['no', 'next time', 'fuck you', 'dont want']))
async def process_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer("or no... FUUUUHKK! I want to play so MUCH!")
    else:
        await message.answer(f"Are you stupid? We are in game now!\nYou have {ATTEMPS} attemps to predict number\nsend me your next prediction")


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_number_answer(message: Message):
        if user['in_game']:
            if int(message.text) == user['secret_number']:
                user['in_game'] = False
                user['total_games'] += 1
                user['wins'] += 1
                await message.answer("O my god, you are genius! Congratulations! Lets play more!")
            elif int(message.text) > user['secret_number']:
                user['attemps'] -= 1
                await message.answer('Мое число меньше')
            elif int(message.text) < user['secret_number']:
                user['attemps'] -= 1
                await message.answer('Мое число больше')

            if user['attemps'] == 0:
                user['in_game'] = False
                user['total_games'] += 1
                await message.answer(
                    f'К сожалению, у вас больше не осталось '
                    f'попыток. Вы проиграли :(\n\nМое число '
                    f'было {user["secret_number"]}\n\nДавайте '
                    f'сыграем еще?'
                )
            else:
                await message.answer('Мы еще не играем. Хотите сыграть?')

@dp.message()
async def process_other_answers(message: Message):
    if user['in_game']:
        await message.answer(
            'Мы же сейчас с вами играем. '
            'Присылайте, пожалуйста, числа от 1 до 100'
        )
    else:
        await message.answer(
            'Я довольно ограниченный бот, давайте '
            'просто сыграем в игру?'
        )


if __name__ == '__main__':
    dp.run_polling(bot)