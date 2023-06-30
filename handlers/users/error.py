from aiogram import types
from loader import dp


@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer(f'Команда {message.text}! \n'
                         f'не найдена, введите /start и затем Общий поиск')
