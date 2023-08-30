#!/usr/local/bin/python
# coding: utf-8
"""
микробот, удаляющий joined chat сообщения в тг
"""

from datetime import datetime
import os
import telebot  # type: ignore
import bot_secrets.py

# =========================================================================
bot = telebot.TeleBot(superhomosecret.SUPERHOMOSECRET)
# =========================================================================
@bot.message_handler(content_types=["text"])
def get_text_messages(message: telebot.types.Message) -> None:
    """
    here is the text message handler
    """
    print(message.chat.id)
@bot.message_handler(content_types=["new_chat_members"])
def handle_new_chat_member_message(message: telebot.types.Message) -> None:
    """
    Обработка (реакция, потом удаление) дурацких сообщений о добавленных пользователях
    """
    status = bot.delete_message(message.chat.id, message.id)
    # если получилось удалить, пишу в лог то, что удалено

# =========================================================================
def main():
    """
    bot operation
    """
    print("diy little helper started!")
    for address in superhomosecret.GENERALINFOADDRESSEE:
        bot.send_message(address, "bot started")
    bot.polling(none_stop=True, interval=5)


# =========================================================================
if __name__ == "__main__":
    main()
# privet
