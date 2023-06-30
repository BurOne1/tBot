from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Поиск по базам', callback_data='General')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Google таблица', callback_data='google_sheet')
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='Вило насосы', callback_data='Pumps'),
                                    #     InlineKeyboardButton(text='Прайс лист', callback_data='Price')
                                    # ],
                                    # [
                                    #     InlineKeyboardButton(text='Запросы Api', callback_data='Wilo'),
                                    #     InlineKeyboardButton(text='Моя команда', callback_data='MyTeam')
                                    # ],
                                    [
                                        InlineKeyboardButton(text='По вопросам работы бота писать в личку',
                                                             url='https://t.me/Grozny473')
                                    ]
                                ])
