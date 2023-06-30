from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Search by article'),
            KeyboardButton(text='My teams'),
        ],
        [
            KeyboardButton(text='My tasks'),
        ],
        [
            KeyboardButton(text='Another text'),
        ],
    ],
    resize_keyboard=True
)
