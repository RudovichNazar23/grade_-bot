from texts import START_MESSAGE, HELP_COMMAND, DESCRIPTION
from aiogram import Bot, Dispatcher, types, executor
from Token import TOKEN
from keyboards import rates_kb, help_kb

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(START_MESSAGE)
    await message.answer(HELP_COMMAND, reply_markup=help_kb)

@dp.message_handler(commands=["help"])
async def help_kommand(message: types.Message):
    await message.answer(text=HELP_COMMAND, reply_markup=help_kb)


@dp.callback_query_handler(text='rates')
async def process_callback_marks(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Please, choose currency', reply_markup=rates_kb)


@dp.callback_query_handler(text='description')
async def process_callback_description(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, DESCRIPTION)


@dp.message_handler()
async def echo(message: types.Message):
    mes_text = message.text
    if "PLN to EUR" in str(mes_text):
        await message.reply("*answer* PLN to EUR")
    elif "PLN to USD" in str(mes_text):
        await message.reply("*answer* PLN to USD")
    elif "PLN to UAH" in str(mes_text):
        await message.reply("*answer* PLN to UAH")


if __name__ == '__main__':
    executor.start_polling(dp)
