from aiogram import types
from loader import dp
from keyboards.default import kb_test
from utils.db_api import quick_commands as commands
from utils.db_api.shermas.my_data import MainDATA


@dp.message_handler(text="MainDATA.new_article")
async def test(message: types.Message):
    dataEx = await commands.select_my_data("3062974")
    await message.answer(f'Hello {message.from_user.full_name}! \n'
                         f'Тут должен быть какой-нибудь текст', reply_markup=kb_test)
