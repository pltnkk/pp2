import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

token = "6055781171:AAFAgvQAXSyxhaVlRLA-xZ_hEwpblANwf58"
bot = telebot.TeleBot('token')

page = 1


@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')

    global page
	#Обработка кнопки - скрыть
    if req[0] == 'unseen':
      bot.delete_message(call.message.chat.id, call.message.message_id)
    elif req[0] == 'next-page':
            if page < 1e9:
                page = page + 1
                markup = InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
                markup.add(InlineKeyboardButton(text=f'<--- Назад', callback_data=f'back-page'),InlineKeyboardButton(text=f'{page}/{10}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->', callback_data=f'next-page'))
                bot.edit_message_text(f'Страница {page} из 10', reply_markup = markup, chat_id=call.message.chat.id, message_id= call.message.message_id)