import sqlite3
import telebot


bot = telebot.TeleBot('6431025245:AAH8oOB21U-XrGpLE1thHDcylsQzUp_ia5o')

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Создать аккаунт', callback_data='create_account'))
    markup.add(telebot.types.InlineKeyboardButton('Найти подругу', callback_data='find_friend'))
    markup.add(telebot.types.InlineKeyboardButton('Админская кнопка', callback_data='admin'))

    bot.send_message(message.chat.id, 'Привет, рад тебя здесь видеть!\nШо нада???', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    def create_account(message):
        conn = sqlite3.connect('database.sql')
        cur = conn.cursor()

        cur.execute(
            'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), pass VARCHAR(50))')
        conn.commit()
        cur.close()
        conn.close()

        bot.send_message(message.chat.id, 'Привет, рад тебя здесь видеть!\nИмя, ты, ху**ша:')
        bot.register_next_step_handler(call.message, user_name)


    def user_name(message):
        name = message.text.strip()
        bot.send_message(call.message.chat.id, 'Enter a password:')
        bot.register_next_step_handler(call.message, user_pass, name)


    def user_pass(message, username):
        conn = sqlite3.connect('database.sql')
        cur = conn.cursor()
        password = message.text.strip()
        conn = sqlite3.connect('database.sql')
        cur = conn.cursor()

        cur.execute('INSERT INTO users (name, pass) VALUES (?, ?)', (username, password))
        conn.commit()

        bot.send_message(call.message.chat.id, 'User registred')


    def delete_user(message):
        user_id = int(message.text.strip())
        conn = sqlite3.connect('database.sql')
        cur = conn.cursor()

        cur.execute('DELETE FROM users WHERE id = ?;', (user_id,))
        conn.commit()

        cur.close()
        conn.close()

        bot.send_message(message.chat.id, "User deleted")

    if call.data == 'create_account':
        bot.send_message(call.message.chat.id, 'hello deat friend\nEnter your name:')
        bot.register_next_step_handler(call.message, user_name)

    elif call.data == 'admin':
        markupAdmin = telebot.types.InlineKeyboardMarkup()
        markupAdmin.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='list_users'))
        markupAdmin.add(telebot.types.InlineKeyboardButton('Удалить Юзера', callback_data='delete_user'))
        markupAdmin.add(telebot.types.InlineKeyboardButton('Третья кнопка', callback_data='delete_users'))
        bot.send_message(call.message.chat.id, 'Здравствуйте, Великий Админ!!!', reply_markup=markupAdmin)

    elif call.data == 'list_users':
        conn = sqlite3.connect('database.sql')
        cur = conn.cursor()

        cur.execute('SELECT * FROM users;')
        users = cur.fetchall()

        cur.close()
        conn.close()


        info = ''
        for el in users:
            info += f'Id: {el[0]}, Name: {el[1]}, password: {el[2]}\n'
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'delete_user':
        bot.send_message(call.message.chat.id, "Id юзера, которого нужно удалить:")
        bot.register_next_step_handler(call.message, delete_user)

    elif call.data == 'delete_users':
        conn = sqlite3.connect('database.sql')
        cur = conn.cursor()
        cur.execute('DELETE FROM users;')
        cur.execute("INSERT INTO users (id, name, pass) VALUES ('1', 'Admin', 'Adminpass');")
        conn.commit()
        bot.send_message(call.message.chat.id, 'Users deleted')
        cur.close()
        conn.close()







bot.polling(none_stop=True)