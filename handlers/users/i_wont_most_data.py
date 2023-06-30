from aiogram import types

from loader import dp

from utils.db_api import quick_commands as commands
from utils.misk import rate_limit


@rate_limit(limit=1)
@dp.message_handler()
async def get_data(message: types.Message):
    text = message.text
    dataEx = await commands.select_my_data(text)
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
                         f'\nОриентировочный срок поставки производства\nна Центральный склад: {dataEx.approximate_delivery_time}\n'
                         f'\nГруппа СТУ: {dataEx.group}')


@rate_limit(limit=1)
@dp.message_handler()
async def get_sec_data(message: types.Message):
    text = await commands.select_my_second_data(message.text)
    await message.answer(f'Артикль: {text.article}\n'
                         f'Описание: {text.description}\n'
                         f'Цена в ЕВРО без НДС: {text.price_eur_without_nds}\n'
                         f'Замена артикля {text.change_article}')
