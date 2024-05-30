from aiogram import Dispatcher
from aiogram.types import Message
import os


from Client.client_keyboard.client_kb import client_kb
from Photo_handler.PhotoHandler import PhotoHandler


PATH_WORKSPACE = 'Workspace'
extensions = ['png',
              'jpg']


async def cmd_start(message: Message):
    await message.answer('''Отправьте фото\nВ одном сообщении - одно фото.
Классы:
1)  Baked chicken
2)  Black bread
3)  Cheese soup
4)  Compote
5)  Fish cutlet
6)  Kharcho
7)  Mashed potatoes
8)  Meat cutlet
9)  Rice
10) White bread''', reply_markup=client_kb)
    await message.delete()


async def save_photo(message: Message):
    try:
        if message.content_type == 'photo':
            name = os.path.join(PATH_WORKSPACE, f'{message.photo[-1].file_unique_id}.png')
            await message.photo[-1].download(name)

        elif message.content_type == 'document':
            if not (message.document.file_name.split('.') in extensions):
                return
            name = os.path.join(PATH_WORKSPACE, f'{message.document.file_unique_id}.png')
            await message.document.download(name)
    except:
        return

    await message.answer_chat_action("typing")

    process = PhotoHandler(name)
    await process.start()
    ans = await process.join()

    # TODO:
    # Добавить базу данных с ценами на продукты

    photo = open(name, 'rb')
    await message.answer_photo(photo)
    await message.answer(f"{ans}")
    os.remove(name)


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