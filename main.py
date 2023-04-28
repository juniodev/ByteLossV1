import telebot
from telebot.types import Message
from generate_response import Chat

class Conversation:
    def __init__(self):
        self.active = False
        self.initialized = False
        self.topic = None

conversations = {}

def process_message(message: Message, chat_id: int, botchat: Chat) -> None:

    if chat_id not in conversations:
        conversations[chat_id] = Conversation()
    
    text = message.text

    chatbot.set_name(message.from_user.first_name)
    bot.send_chat_action(chat_id, action='typing')

    response = botchat.processar_pergunta(text)

    bot.reply_to(message, response)

if __name__ == "__main__":

    bot = telebot.TeleBot("YOUR_TELEGRAM_API_TOKEN")

    chatbot = Chat()

    chatbot.init_bot()

    @bot.message_handler(func=lambda message: True)
    def handle_message(message: Message) -> None:
        chat_id = message.chat.id
        process_message(message, chat_id, botchat=chatbot)

    bot.polling(skip_pending=True)
