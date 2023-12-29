import telebot
import requests
import json

bot = telebot.TeleBot('6431025245:AAH8oOB21U-XrGpLE1thHDcylsQzUp_ia5o')
API = '7dc66b9679a6767fb39195ad41e433cc'

#https://api.openweathermap.org/data/2.5/weather?q=London&appid=7dc66b9679a6767fb39195ad41e433cc&&lang=ru&&units=metric
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

@bot.message_handler(commands=['start'])
def main(message):
    # markup=types.InlineKeyboardMarkup()
    # btn1 = types.InlineKeyboardButton('google', url='google.com')
    # btn2 = types.InlineKeyboardButton('Delete message', callback_data='delete')
    # btn3 = types.InlineKeyboardButton('Edit message', callback_data='edit')
    # markup.row(btn1)
    # markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Helloy, insert name of city') #, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&lang=ru&&units=metric')
    data = json.loads(res.text)
    if "weather" in data:
        bot.reply_to(message, f'Сейчас в городе {data["name"]} {data["weather"][0]["description"]} \nТемпература: {round(data["main"]["temp"])}°C, \nощущается как {round(data["main"]["feels_like"])}°C\nдавление: {data["main"]["pressure"]}\nвлажность: {data["main"]["humidity"]}')
    else:
        bot.reply_to(message, 'Извините, не удалось получить информацию о погоде для данного города.')
bot.polling(none_stop=True)