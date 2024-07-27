import telebot
from langchain.schema import HumanMessage, SystemMessage
from langchain_community.chat_models.gigachat import GigaChat
import requests
import re
from config import TELEGRAM_TOKEN, GIGACHAT_TOKEN

# Авторизация в GigaChat
chat = GigaChat(credentials=GIGACHAT_TOKEN, verify_ssl_certs=False)

# Создание бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def generate_response(system_prompt, user_message):
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_message)
    ]
    response = chat.invoke(messages)
    return response.content

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш помощник для хакатона. Чем могу помочь?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    system_prompt = load_prompt_from_gdrive('https://docs.google.com/document/d/1cnQ-YaeQeHnOcMKSrctlPYi73jkvSAn-OlQNLiQ6ieA/export?format=txt')
    response = generate_response(system_prompt, user_message)
    bot.reply_to(message, response)

def load_prompt_from_gdrive(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

if __name__ == "__main__":
    bot.polling()
