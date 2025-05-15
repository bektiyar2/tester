import telebot

# Замените 'YOUR_TOKEN' на токен вашего бота
bot = telebot.TeleBot('YOUR_TOKEN')

# Замените 'TO_CHAT_ID' на ID группы, в которую нужно пересылать сообщения
TO_CHAT_ID = 'TO_CHAT_ID'

@bot.message_handler(content_types=['text'])
def forward_message(message):
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)

if __name__ == '__main__':
    bot.polling(none_stop=True)
