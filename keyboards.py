from telegram import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Daily completedAt', callback_data='type:daily'), InlineKeyboardButton(text='Weekly completedAt', callback_data='type:weekly')],
        [InlineKeyboardButton(text='Monthly completedAt', callback_data='type:monthly'), InlineKeyboardButton(text='Total completedAt', callback_data='type:total_completeat')]
    ]
)