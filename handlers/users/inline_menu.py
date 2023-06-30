from keyboards.default import kb_test
from keyboards.inline import ikb_menu
from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery
from utils.db_api import quick_commands as commands

from utils.db_api.quick_commands import select_all_users
from utils.db_api.shermas.user import User


@dp.callback_query_handler(text='MyTeam')
async def send_message(call: CallbackQuery):
    test = await commands.select_all_users()
    print(test)
    # await call.message.answer(f'Hehehehe {test}')
