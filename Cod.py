import telebot
from telebot import types

# Токен вашего бота
TOKEN = '6678216454:AAH6CEN1d7_Rhc9olvbPxUoo6vGRAftrtSA'
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствую Вячеслав Петрович, вот статистика за 22.12.2023 [http://127.0.0.1:8050/]. Выберите услугу для установки временного лимита!")
    menu(message)


def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🖥 Компьютеры")
    btn2 = types.KeyboardButton("🎮 VR шлема")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Выберите устройство", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "🖥 Компьютеры")
def comp(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1️⃣")
    btn2 = types.KeyboardButton("2️⃣")
    btn3 = types.KeyboardButton("3️⃣")
    btn4 = types.KeyboardButton("4️⃣")
    markup.add(btn1, btn2)
    markup.add(btn4, btn3)
    bot.send_message(message.chat.id, 'На какой компьютер установить лимит?', reply_markup=markup)
    bot.register_next_step_handler(message, compig)


def compig(message):
    if message.text in ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1️⃣")
        btn2 = types.KeyboardButton("2️⃣")
        btn3 = types.KeyboardButton("4️⃣")
        btn4 = types.KeyboardButton("1️⃣2️⃣")
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите на какой срок (час) предоставляется услуга', reply_markup=markup)
        bot.register_next_step_handler(message, compsfinish)


def compsfinish(message):
    bot.send_message(message.chat.id, 'Услуга запущена, ограничения установлены')
    menu(message)


@bot.message_handler(func=lambda message: message.text == "🎮 VR шлема")
def vr(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1️⃣")
    btn2 = types.KeyboardButton("2️⃣")
    btn3 = types.KeyboardButton("3️⃣")
    btn4 = types.KeyboardButton("4️⃣")
    markup.add(btn1, btn2)
    markup.add(btn4, btn3)
    bot.send_message(message.chat.id, 'На какое устройство устройство установить лимит?', reply_markup=markup)
    bot.register_next_step_handler(message, vrig)


def vrig(message):
    if message.text in ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1️⃣")
        btn2 = types.KeyboardButton("2️⃣")
        btn3 = types.KeyboardButton("3️⃣")
        btn4 = types.KeyboardButton("4️⃣")
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите на какой срок (час) предоставляется услуга', reply_markup=markup)
        bot.register_next_step_handler(message, vrfinish)


def vrfinish(message):
    bot.send_message(message.chat.id, 'Услуга запущена, ограничения установлены')
    menu(message)


# Запускаем бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
