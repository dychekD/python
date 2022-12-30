import telebot
import random

bot = telebot.TeleBot("Token")

@bot.message_handler(commands=['rules'])
def send_welcome(message):
	bot.send_message(message.chat.id,'There are 117 candies on the table.\n'
    'You and bot can take up to 28 candies in their turn.\n' 
    'The player who takes last candies from the table gets all candies')

candy_left = 117

def check (candy_left, winner):
    if candy_left > 0:
        game_vs_bot (message) 
    else: 
        candy_left = 117
        if winner == True:
            winner = False
        elif winner == False:
            winner = True
        if winner == True:
            result = 'You have won'
        else: result = 'I have won'  
    return result


@bot.message_handler(content_types=['text'])
def game_vs_bot (message):
    m = message.text
    turn = int(m)
    global candy_left
    candy_left = candy_left - turn
    global winner
    winner = False    
    bot.send_message (message.chat.id, text=f'Candy left: {candy_left}')
    if candy_left > 0:
        if candy_left <= 28:
            temp = candy_left
            bot.send_message (message.chat.id, text=f'My turn. I have taken {temp} candies')
            candy_left = 0
            winner = True
            bot.send_message (message.chat.id, text=f'{check (candy_left, winner)}')
            candy_left = 117
        else:
            temp = random.randint (1, 28)
            bot.send_message (message.chat.id, text=f'My turn. I have taken {temp} candies') 
            candy_left = candy_left - temp
            bot.send_message (message.chat.id, text=f'Your turn. Candy left: {candy_left}') 
            winner = True        
    else: 
        bot.send_message (message.chat.id, text=f'{check (candy_left, winner)}')
        candy_left = 117


bot.infinity_polling()