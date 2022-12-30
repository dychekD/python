import json
import requests
import telebot
from telebot import types

bot = telebot.TeleBot("Tocken")

response = requests.get ('https://www.cbr-xml-daily.ru/daily_json.js')
result = json.loads (response.text)
USD = round (result ['Valute']['USD']['Value'], 2)
EUR = round (result ['Valute']['EUR']['Value'], 2)
AMD = round (result ['Valute']['AMD']['Value'], 2)
TRY = round (result ['Valute']['TRY']['Value'], 2)

@bot.message_handler(commands=['currency'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("USD")
    item2 = types.KeyboardButton("EUR")
    item3 = types.KeyboardButton("AMD")
    item4 = types.KeyboardButton("TRY")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,'Please select currency',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "USD"):
        bot.send_message(message.chat.id, text=f'Exchange rate for US dollar today: 1 USD = {USD} rubles')
    elif(message.text == "EUR"):
        bot.send_message(message.chat.id, text=f'Exchange rate for euro today: 1 EUR = {EUR} rubles')
    elif(message.text == "AMD"):
        bot.send_message(message.chat.id, text=f'Exchange rate for Armenian dram today: 100 AMD = {AMD} rubles')
    
    elif message.text == "TRY":
        bot.send_message(message.chat.id, text=f'Exchange rate for Turkish lira today: 10 TRY = {TRY} rubles')
    else:
        bot.send_message(message.chat.id, text="Select currency on the button")

bot.infinity_polling()


