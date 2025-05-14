import telebot

# Константы для API токена и ID чатов
API_TOKEN = '7705828331:AAES0Sp5mAFYQA11qinCmdZcraMgvRgI1nY'
SOURCE_CHAT_ID = '-1002690977824'
DESTINATION_CHAT_ID = '-1002650951724'

# Создаем бота с помощью токена
bot = telebot.TeleBot(API_TOKEN)

# Обработчик сообщений
@bot.message_handler(content_types=['text', 'photo', 'document', 'audio', 'video'])
def forward_message(message):
    """Функция для пересылки сообщений из одного чата в другой."""
    bot.forward_message(DESTINATION_CHAT_ID, message.chat.id, message.message_id)

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
