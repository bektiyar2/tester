import telebot
import requests
import threading
import time

# Замените 'YOUR_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7705828331:AAES0Sp5mAFYQA11qinCmdZcraMgvRgI1nY')

# Замените 'TO_CHAT_ID' на ID группы, в которую нужно пересылать сообщения
TO_CHAT_ID = '-1002650951724'

# URL вашего веб-сервиса
url = "https://tester-nqi6.onrender.com"

# Интервал между запросами в секундах (например, 10 минут)
interval = 600

def keep_alive():
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Сервис работает нормально.")
            else:
                print(f"Ошибка: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения: {e}")
        
        # Ожидание перед следующим запросом
        time.sleep(interval)

# Запуск keep_alive в отдельном потоке
threading.Thread(target=keep_alive).start()

@bot.message_handler(content_types=['text'])
def forward_message(message):
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
