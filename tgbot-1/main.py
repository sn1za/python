import telebot
from telebot import types


bot = telebot.TeleBot('6431025245:AAH8oOB21U-XrGpLE1thHDcylsQzUp_ia5o')


@bot.message_handler(commands=['start'])
def main(message):
    markup=types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('google', url='google.com')
    btn2 = types.InlineKeyboardButton('Delete message', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Edit message', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Helloy, mir!\nManera krytit mir ya paladin!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id )
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('XYI', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['help'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('google')
    btn2 = types.KeyboardButton('Delete message')
    btn3 = types.KeyboardButton('Edit message')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Poshel nahui!\nYa tebe chto besplatniy???', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'google':
        bot.send_message(message.chat.id, 'Red')


@bot.message_handler(commands=['test1'])
def main(message):
    bot.send_message(message.chat.id, f'Helloy, uvazhaemiy {message.from_user.first_name} {message.from_user.last_name}, chem mogy pomoch?')


@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler()
def main(message):
    bot.send_message(message.chat.id, 'cho ti pishesh chepyha??')

bot.polling(none_stop=True)