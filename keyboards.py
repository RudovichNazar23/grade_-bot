from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

"""START KEYBOARD (rates_kb)"""
PLN_to_EUR_button = KeyboardButton('PLN to EUR')
PLN_to_Usd_button = KeyboardButton('PLN to USD')
PLN_to_UAH_button = KeyboardButton('PLN to UAH')
help_option = "/help"

rates_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
rates_kb.add(PLN_to_EUR_button)
rates_kb.add(PLN_to_Usd_button)
rates_kb.add(PLN_to_UAH_button)
rates_kb.add(help_option)
""""""


"""HELP KEYBOARD (help_kb)"""

inline_btn_1 = InlineKeyboardButton('rates - currency exchange rate', callback_data='rates')
inline_btn_2 = InlineKeyboardButton('description - description of the bot', callback_data='description')
help_kb = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)
""""""
