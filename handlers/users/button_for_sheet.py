import httplib2

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline import ikb_menu
from loader import dp

from states import GoogleSheet


@dp.callback_query_handler(text='google_sheet')
async def sheet_(call: CallbackQuery):
    await call.message.answer('Напиши мне Артикул и я тебе\nпомогу найти оборудование')
    await GoogleSheet.test1.set()


@dp.message_handler(state=GoogleSheet.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test1=answer)
    data = await state.get_data()
    name = data.get('test1')
    path_json = "E:/AlgoInvect/python/firstBot/creds/energoprof-387808-a62ef73bdda0.json"
    # path_json = "/home/c76382/testbottelegram.na4u.ru/www/creds/energoprof-387808-a62ef73bdda0.json"

    creds_auth = ServiceAccountCredentials \
        .from_json_keyfile_name(path_json, ['https://www.googleapis.com/auth/spreadsheets']) \
        .authorize(httplib2.Http())

    service = build('sheets', 'v4', http=creds_auth)

    sss = service.spreadsheets()

    wilo_id = "1k2HNdWadastO5xhkW6BA3WTkpxDYHPxdhromodR9RL4"

    r_w = sss.values().get(spreadsheetId=wilo_id, range="Wilo!A4:B24").execute()
    gg = r_w.get('values', [])
    num = [0, 0]
    for index1 in range(len(gg)):
        for index2 in range(0, 2, 1):
            if gg[index1][index2] == name:
                print("Yes")
                num = [index1, index2]

    val = num[0] + 4

    next_r = sss.values().get(spreadsheetId=wilo_id, range=f"Wilo!A{val}:K{val}").execute()

    ll = next_r.get('values', [])
    await message.answer(
        f'Новый артикул: {ll[0][0]}\n'
        f'Старый артикул: {ll[0][1]}\n'
        f'Наименование: {ll[0][2]}\n'
        f'Кол-во КЭП: {ll[0][3]}\n'
        f'Кол-во ЭП: {ll[0][4]}\n'
        f'Резерв: {ll[0][5]}\n'
        f'Объект: {ll[0][6]}\n'
        f'Нужно: {ll[0][7]}\n'
        f'Заказ: {ll[0][8]}\n'
        f'Заказано: {ll[0][9]}\n'
        # f'КМинимальная цена для клиента\nна СТАРЫЙ артикул: {ll[0][10]}\n'
    )
    # print(gg[0][2])

    await message.answer(f'Рад был помочь', reply_markup=ikb_menu)
    await state.finish()
