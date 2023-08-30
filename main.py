#!/usr/local/bin/python
# coding: utf-8
"""
микробот, удаляющий joined chat сообщения в тг
"""

from datetime import datetime
import os
import telebot  # type: ignore
import bot_secrets

# =========================================================================
bot = telebot.TeleBot(bot_secrets.LHSECRET)
# =========================================================================
#@bot.message_handler(content_types=["text"])
#def get_text_messages(message: telebot.types.Message) -> None:
#    """
#    here is the text message handler
#    """
#    print(message.chat.id)
# =========================================================================
@bot.message_handler(content_types=["new_chat_members", "left_chat_member"])
def handle_new_chat_member_message(message: telebot.types.Message) -> None:
    """
    Обработка (удаление + лог) дурацких сообщений о добавленных пользователях
    """
    if (message.chat.type in ("group", "supergroup")): # обслуживаем только группы
        status = bot.delete_message(message.chat.id, message.id) #удаляем сообщение
        for address in bot_secrets.GENERALINFOADDRESSEE: # пишем о событии всем желающим
            bot.send_message(address, 
                f"status message from username {message.from_user.username} " 
                f"(id={message.from_user.id}, name={message.from_user.first_name}) "
                f"deleted in {message.chat.title} with {status=}"
                f" message type is '{message.content_type}'"
                )
# =========================================================================
def main():
    """
    bot operation
    """
    print("diy little helper started!")
    for address in bot_secrets.GENERALINFOADDRESSEE:
        bot.send_message(address, "bot started")
    bot.polling(none_stop=True, interval=5)


# =========================================================================
if __name__ == "__main__":
    main()
# privet
