from aiogram import Dispatcher
from aiogram.types import Message
import os


from Client.client_keyboard.client_kb import client_kb
from Photo_handler.PhotoHandler import PhotoHandler
from create_bot import database


PATH_WORKSPACE = 'Workspace'
extensions = ['png',
              'jpg']


async def cmd_start(message: Message):
    await message.answer('''Отправьте фото\nВ одном сообщении - одно фото.
Классы:
1) Запеченная курица
2) Черный хлеб
3) Сырный суп
4) Компот
5) Рыбные котлеты
6) Харчо
7) Картофельное пюре
8) Мясные котлеты
9) Рис
10) Белый хлеб''', reply_markup=client_kb)
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

    ans_message = ''
    cost = 0
    for product in ans:
        c = await database.get_cost(product[0])
        c *= product[1]

        s3 = f'{c} руб.'
        s3 += " " * (4 - len(s3))
        s1 = f"{product[0]}"
        s1 += " " * (17 - len(s1))
        s2 = f"{product[1]} шт."
        s2 += " " * (4 - len(s2))
        ans_message += f"{s1} {s2} {s3}\n"
        cost += c
    ans_message += f'Общая стоимость:        {cost} руб.'
    print(ans_message)

    # TODO:
    # Добавить базу данных с ценами на продукты

    photo = open(name, 'rb')
    await message.answer_photo(photo)
    await message.answer(f"<code>{ans_message}</code>", parse_mode='HTML')
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