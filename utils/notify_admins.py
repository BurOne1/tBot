import logging

from aiogram import Dispatcher

from data.config import admins_id

#запускаем асинзронную функцию on_startup_notify, получаем id админов и пытаемся отправить им сообщения


async def on_startup_notify(dp: Dispatcher):
    for admin in admins_id:
        try:
            text = 'Bot is working'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
