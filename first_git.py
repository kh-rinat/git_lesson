from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message
from bot_config import git_lesson_bot_API

BOT_TOKEN = git_lesson_bot_API

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

admin_ids: list[int] = [680554251,173901673]

class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

@dp.message(IsAdmin(admin_ids))
async def process_if_admin(message: Message):
    await message.answer("You are admin")

@dp.message()
async def process_not_admin(message: Message):
    await message.answer("You are not admin")

if __name__ == '__main__':
    dp.run_polling(bot)