import telebot
import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Получаем значения из переменных окружения
TOKEN = os.getenv('BOT_TOKEN')
TO_CHAT_ID = os.getenv('CHAT_ID')

# Проверка, что переменные загружены
if not TOKEN or not TO_CHAT_ID:
    print("Ошибка: Переменные BOT_TOKEN или CHAT_ID не найдены в файле .env")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice', 'sticker'])
def forward_message(message):
    try:
        # Пересылаем сообщение в указанный чат
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        print(f"Сообщение от {message.from_user.first_name} (ID: {message.from_user.id}) переслано.")
    except Exception as e:
        print(f"Ошибка при пересылке: {e}")

if __name__ == '__main__':
    print("Бот запущен и использует настройки из .env...")
    bot.infinity_polling()
