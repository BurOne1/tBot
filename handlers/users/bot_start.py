from aiogram import types

from keyboards.inline import ikb_menu
from loader import dp

from filters import IsPrivate
from utils.db_api import quick_commands as commands
from utils.db_api.shermas.my_data import MainDATA
from utils.misk import rate_limit


@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет {user.first_name}\n'
                                 f'Выбери что тебе надо найти', reply_markup=ikb_menu)
        elif user.status == 'baned':
            await message.answer('Я с тобой не дружу!')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active')
        await message.answer('Ты зарегистрирован')


@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/ban')
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='baned')
    await message.answer('С этого момента не дружим.')


@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/unban')
async def get_unban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='active')
    await message.answer('Мы снова дружим, но уже не так как раньше')


@rate_limit(limit=3)
@dp.message_handler(text='/profile')
async def get_profile(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'ID - {user.user_id}\n'
                         f'First name - {user.first_name}\n'
                         f'Last name - {user.last_name}\n'
                         f'Username - {user.username}\n'
                         f'Status - {user.status}\n')




