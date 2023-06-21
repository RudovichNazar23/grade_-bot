from texts import TOKEN, START_MESSAGE, HELP_COMMAND, DESCRIPTION
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
bot = Bot(TOKEN)
dp = Dispatcher(bot)


# keyboards.py
inline_btn_1 = InlineKeyboardButton('#1 button', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('#2 button', callback_data='button2')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)

#bot.py
@dp.message_handler(commands=['start'])
async def process_command_1(message: types.Message):
    await message.answer("Please, pick the period", reply_markup=help_kb)

@dp.callback_query_handler(text='button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Button #1')

@dp.callback_query_handler(text='button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Button #2')

if __name__ == '__main__':
    executor.start_polling(dp)