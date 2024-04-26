from aiogram import Dispatcher
from aiogram.types import Message
import os
import json


from Client.client_keyboard.client_kb import client_kb


PATH_WORKSPACE = 'Workspace'
PATH_DATA = os.path.join('Workspace', 'Data')
PATH_NUMBER = os.path.join('Workspace', 'Number.json')


async def cmd_start(message: Message):
    await message.answer('Отправьте фото', reply_markup=client_kb)
    await message.delete()


async def save_photo(message: Message):
    for img in message.photo:

        with open(PATH_NUMBER, 'r') as file:
            number = json.load(file)

        name = os.path.join(PATH_DATA, f'{number}.png')
        await img.download(name)

        number += 1
        with open(PATH_NUMBER, 'w') as file:
            json.dump(number, file)


async def delete_message(message: Message):
    await message.delete()


def register_client_router(dp: Dispatcher):
    dp.register_message_handler(cmd_start,
                                commands=['start'])

    dp.register_message_handler(cmd_start,
                                commands=['help'])

    dp.register_message_handler(delete_message)