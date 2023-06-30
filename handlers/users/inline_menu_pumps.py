from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from utils.db_api import quick_commands as commands
from keyboards.inline import ikb_menu
from loader import dp

from states import Pumps


@dp.callback_query_handler(text='Pumps')
async def pumps_(call: CallbackQuery):
    await call.message.answer('Напиши мне Артикул и я тебе\nпомогу найти оборудование')
    await Pumps.test1.set()


@dp.message_handler(state=Pumps.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test1=answer)
    data = await state.get_data()
    name = data.get('test1')
    try:
        dataEx = await commands.select_my_data(name)
        await message.answer(f'Тип оборудования: {dataEx.type_o}\n'
                             f'\nГруппа продуктов: {dataEx.product_group}\n'
                             f'\nВозможность сборки\nисходя из наличия компонентов: {dataEx.availability_of_comp}\n'
                             f'\nНовый артикль: {dataEx.new_article}\n'
                             f'\nСтарый артикул: {dataEx.old_article}\n'
                             f'\nНаименование: {dataEx.name}\n'
                             f'\nЦена 2023 в евро, с НДС 20%: {dataEx.price_in_euro}\n'
                             f'\nЦена 2023 в рублях, с НДС 20%: {dataEx.price_in_rub}\n'
                             f'\nГруппа скидки: {dataEx.discount_group}\n'
                             f'\nEAN/UPCкод: {dataEx.ean_upc_code}\n'
                             f'\nВес нетто, кг: {dataEx.net_weight_kg}\n'
                             f'\nВес брутто,кг: {dataEx.gross_weight_kg}\n'
                             f'\nДлина без учета упаковки, мм: {dataEx.length_excluding_packaging_mm}\n'
                             f'\nШирина без учета упаковки,мм: {dataEx.width_excluding_packaging_mm}\n'
                             f'\nВысота без учета упаковки, мм: {dataEx.height_without_packaging_mm}\n'
                             f'\nОриентировочный срок поставки производства\nна Центральный склад:'
                             f' {dataEx.approximate_delivery_time}\n'
                             f'\nГруппа СТУ: {dataEx.group}')
    except Exception:
        await message.answer(f'Атрикул {name} не найден!')

    await message.answer(f'Рад был помочь', reply_markup=ikb_menu)
    await state.finish()



