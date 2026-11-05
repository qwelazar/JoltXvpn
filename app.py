import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("🌐 Мой VPN"),
        KeyboardButton("🆘 Помощь")
    )

    bot.send_message(
        message.chat.id,
        "Добро пожаловать в JoltXvpn! ⚡\n\n"
        "Твой быстрый и надёжный VPN.",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: message.text == "🌐 Мой VPN")
def my_vpn(message):
    bot.send_message(
        message.chat.id,
        "Подписка пока не настроена. Скоро здесь появится твой VPN!"
    )

@bot.message_handler(func=lambda message: message.text == "🆘 Помощь")
def help_user(message):
    bot.send_message(
        message.chat.id,
        "Поддержка JoltXvpn скоро будет доступна."
    )

bot.infinity_polling()

