from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from utils.db_api import quick_commands as commands
from keyboards.inline import ikb_menu
from loader import dp

from states import Price


@dp.callback_query_handler(text='Price')
async def register_(call: CallbackQuery):
    await call.message.answer('Напиши мне Артикул и я тебе\n помогу найти цену оборудования')
    await Price.test1.set()


@dp.message_handler(state=Price.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test1=answer)
    data = await state.get_data()
    name = data.get('test1')
    try:
        text = await commands.select_my_second_data(name)
        await message.answer(f'Артикул: {text.article}\n'
                             f'Описание: {text.description}\n'
                             f'Цена в ЕВРО без НДС: {text.price_eur_without_nds}\n'
                             f'Замена артикула {text.change_article}')

    except Exception:
        await message.answer(f'Атрикул {name} не найден!')

    await message.answer(f'Рад был помочь', reply_markup=ikb_menu)
    # await register.test2.set()

    # @dp.message_handler(state=register.test2)
    # async def state2(message: types.Message, state: FSMContext):
    #     answer = message.text
    #
    #     await state.update_data(test2=answer)
    #     data = await state.get_data()
    #     name = data.get('test1')
    #     years = data.get('test2')
    #     await message.answer(f'Регистрация успешно завершина {name}', reply_markup=kb_menu)

    await state.finish()
