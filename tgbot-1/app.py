import sqlite3
import telebot


bot = telebot.TeleBot('6431025245:AAH8oOB21U-XrGpLE1thHDcylsQzUp_ia5o')

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), pass VARCHAR(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id,'hello deat friend\nEnter your name:')
    bot.register_next_step_handler(message, user_name)


    # if call.data == 'create_account':
    #     bot.send_message(call.message.chat.id, 'hello deat friend\nEnter your name:')
    #     bot.register_next_step_handler(call.message, user_name)



def user_name(message):
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Enter a password:')
    bot.register_next_step_handler(message, user_pass, name)


def user_pass(message, username):
    password = message.text.strip()
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass) VALUES (?, ?)', (username, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('List of Users', callback_data='users'))
    markup.add(telebot.types.InlineKeyboardButton('Clear list of Users', callback_data='delete_users'))
    bot.send_message(message.chat.id, 'User registred', reply_markup=markup)
    #bot.register_next_step_handler(message, user_pass)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()

    if call.data == 'users':
        cur.execute('SELECT * FROM users;')
        users = cur.fetchall()

        info = ''
        for el in users:
            info += f'Id: {el[0]}, Name: {el[1]}, password: {el[2]}\n'
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'delete_users':
        cur.execute('DELETE FROM users;')
        cur.execute("INSERT INTO users (id, name, pass) VALUES ('Admin', 'Adminpass');")
        conn.commit()
        bot.send_message(call.message.chat.id, 'Users deleted')

    cur.close()
    conn.close()




@bot.message_handler(commands=['list'])
def list(message):
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Id: {el[0]}, Name: {el[1]}, password: {el[2]}\n'

    cur.close()
    conn.close()

    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['delete-user'])
def delete(message):
    bot.send_message(message.chat.id, "input userid for delete user:")
    bot.register_next_step_handler(message, delete_user)

def delete_user(message):
    user_id = int(message.text.strip())
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()

    cur.execute('DELETE FROM users WHERE id = ?;', (user_id,))
    conn.commit()

    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "User deleted")

bot.polling(none_stop=True)





