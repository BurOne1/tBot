import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from data.config import API_TOKEN
from keyboards.default.keyboard_test import kb_test
from keyboards.inline import ikb_menu
from loader import dp
from states.test import Wilo


@dp.callback_query_handler(text='Wilo')
async def pumps_(call: CallbackQuery):
    await call.message.answer('Напиши мне Город склад которого\nтебя интересует', reply_markup=kb_test)
    await Wilo.test1.set()


code = ''


@dp.message_handler(state=Wilo.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test1=answer)
    data = await state.get_data()
    name = data.get('test1')

    if name == 'Екатеринбург':
        state1.code = '2561'
        await message.answer(f'Введи артикул котырый\nхочешь найти на складе в {name}')
        await Wilo.test2.set()
    elif name == 'Ногинск':
        state1.code = '2531'
        await message.answer(f'Введи артикул котырый\nхочешь найти на складе в {name}')
        await Wilo.test2.set()
    else:
        await message.reply("Город указан неверно")


@dp.message_handler(state=Wilo.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test2=answer)
    data = await state.get_data()
    name = data.get('test2')

    try:
        r = requests.get(
            f"https://wilo.market/export/{API_TOKEN}/stock-remains/{state1.code}/json/"
        )
        data = r.json()
        print(data)

        for index in range(len(data)):
            if data[index]["Sku"] == name:
                print("Yes")
                num = index

        # for index in range(len(data)):
        await message.answer(f'Артикул: {data[num]["Sku"]}\n'
                             f'Наименование: {data[num]["Name"]}\n'
                             f'Колличество: {data[num]["Quantity"]}\n'
                             f'Город: {data[num]["City"]}\n'
                             f'Имя партнёра: {data[num]["PartnerName"]}\n'
                             f'Контактная персона: {data[num]["ContactPerson"]}\n'
                             f'Номер Телефона: {data[num]["PhoneNumber"]}\n'
                             f'Email: {data[num]["Email"]}\n'
                             f'Обнавлено: {data[num]["UpdateDate"]}\n'
                             f'Комментарий: {data[num]["Comments"]}\n')

    except Exception as ex:
        print(ex)
        print("Mayby you stupid")
        await message.answer(f'Ошибка получения API')

    await message.answer(f'Рад был помочь', reply_markup=ikb_menu)
    await state.finish()
