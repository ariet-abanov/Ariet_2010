import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import dotenv_values
import logging
from random import choice

token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
dp = Dispatcher()

how_many_user_use_bot = 0

name_list = ['Ariet', 'Atai', 'Agahan', 'Nurdoolot', 'Umarali', 'Elnur']

unique_users = set()
@dp.message(Command('start'))
async def command_start(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name

    if user_id not in unique_users:
        unique_users.add(user_id)

    unique_user_count = len(unique_users)
    await message.answer(f'Привет {name}, наш бот обслуживает уже {unique_user_count} пользователей!')

@dp.message(Command('myinfo'))
async def my_info(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    user_name = message.from_user.username
    await message.answer(f'Ваш id:{user_id}, Имя:{first_name}, Имя_пользователя:{user_name}')

@dp.message(Command('random'))
async def random_name(message: types.Message):
    await message.answer(choice(name_list))


async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())