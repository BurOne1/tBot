import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import API_TOKEN
from utils.db_api import quick_commands as commands
from keyboards.inline import ikb_menu
from loader import dp

from states import General

# цена наименование рубли и евро

@dp.callback_query_handler(text='General')
async def general_(call: CallbackQuery):
    await call.message.answer('Напиши мне Артикул и я тебе\nразгадаю все его тайны!!!')
    await General.test1.set()


@dp.message_handler(state=General.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test1=answer)
    data = await state.get_data()
    name = data.get('test1')
    try:
        excel1 = await commands.select_my_data(name)
        await message.answer(
                             f'\nЦена 2023 в евро, с НДС 20%: {excel1.price_in_euro}\n'
                             f'Цена 2023 в рублях, с НДС 20%: {excel1.price_in_rub}\n')

    except Exception:
        print(Exception)
        # await message.answer(f'Атрикул {name} не найден в 1 Excel файле')

    try:
        excel2 = await commands.select_my_second_data(name)
        await message.answer(f'Артикул: {excel2.article}\n'
                             f'Описание: {excel2.description}\n'
                             f'Цена в ЕВРО без НДС: {excel2.price_eur_without_nds}\n'
                             f'Замена артикула {excel2.change_article}')

    except Exception:
        print(Exception)
        # await message.answer(f'Атрикул {name} не найден во 2 Excel файле')

    try:
        r = requests.get(
            f"https://wilo.market/export/{API_TOKEN}/stock-remains/2561/json/"
        )
        data = r.json()
        # print(data)

        for index in range(len(data)):
            if data[index]["Sku"] == name:
                print("Yes")
                num = index

        # for index in range(len(data)):
        await message.answer(f'Город: {data[num]["City"]}\n\n'
                             f'Артикул: {data[num]["Sku"]}\n'
                             f'Наименование: {data[num]["Name"]}\n'
                             f'Колличество: {data[num]["Quantity"]}\n')

    except Exception as ex:
        print(ex)
        # await message.answer(f'Нет данных по Api из Екатеринбурга')

    try:
        r = requests.get(
            f"https://wilo.market/export/{API_TOKEN}/stock-remains/2531/json/"
        )
        data = r.json()
        # print(data)

        for index in range(len(data)):
            if data[index]["Sku"] == name:
                print("Yes")
                num2 = index

        # for index in range(len(data)):
        await message.answer(f'Город: {data[num2]["City"]}\n\n'
                             f'Артикул: {data[num2]["Sku"]}\n'
                             f'Наименование: {data[num2]["Name"]}\n'
                             f'Колличество: {data[num2]["Quantity"]}\n')

    except Exception as ex:
        print(ex)
        # await message.answer(f'Нет данных по Api из Ногинска')

    await message.answer(f'Рад был помочь', reply_markup=ikb_menu)
    await state.finish()
