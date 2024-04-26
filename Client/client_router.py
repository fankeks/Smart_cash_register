from aiogram import Dispatcher
from aiogram.types import Message
import os
import json


from Client.client_keyboard.client_kb import client_kb


PATH_WORKSPACE = 'Workspace'
PATH_DATA = os.path.join('Workspace', 'Data')
PATH_NUMBER = os.path.join('Workspace', 'Number.json')


async def cmd_start(message: Message):
    await message.answer('Отправьте фото\nВ одном сообщении - одно фото', reply_markup=client_kb)
    await message.delete()


async def save_photo(message: Message):
    with open(PATH_NUMBER, 'r') as file:
        number = json.load(file)

    name = os.path.join(PATH_DATA, f'{number}.png')

    if message.content_type == 'photo':
        await message.photo[-1].download(name)
    elif message.content_type == 'document':
        await message.document.download(name)

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

    dp.register_message_handler(save_photo,
                                content_types=['photo', 'document'])

    dp.register_message_handler(delete_message)