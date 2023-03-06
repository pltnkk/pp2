import aiogram
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.utils import executor

bot = Bot(token = "6055781171:AAFAgvQAXSyxhaVlRLA-xZ_hEwpblANwf58")
dp = Dispatcher(bot)


@dp.message_handler(commands = ['start'])
async def welcome(message: types.Message):
    await message.reply("Привет")
