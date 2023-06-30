from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Екатеринбург'),
        ],
        [
            KeyboardButton(text='Ногинск'),
        ]
    ],
    resize_keyboard=True
)