from aiogram import types
from loader import dp

@dp.message_handler(text='Search by article')
async def button_test(message: types.Message):
    await message.answer(f'{message.from_user.full_name}! \n'
                         f'напиши артикль который тебе нужен')


@dp.message_handler(text='My tasks')
async def button_test(message: types.Message):
    await message.answer(f'Твои задачи {message.from_user.full_name}! \n'
                         f'1\n'
                         f'2\n'
                         f'3\n')