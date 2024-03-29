#!/usr/local/bin/python
# coding: utf-8
"""
микробот, удаляющий joined chat сообщения в тг
"""
import asyncio
from datetime import datetime
import os
import bot_secrets
import telebot # type: ignore
from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot(bot_secrets.LHSECRET) # get token from @BotFather
# =========================================================================
# =========================================================================
#@bot.message_handler(content_types=["text"])
#def get_text_messages(message: telebot.types.Message) -> None:
#    """
#    here is the text message handler
#    """
#    print(message.chat.id)
# =========================================================================
@bot.message_handler(content_types = ["new_chat_members", "left_chat_member"])
async def handle_new_chat_member_message(message: telebot.types.Message) -> None:
    """
    Обработка (удаление + лог) дурацких сообщений о добавленных пользователях
    """
    if (message.chat.type in ("group", "supergroup")): # обслуживаем только группы
        status = await bot.delete_message(message.chat.id, message.id) #удаляем сообщение
        markup = telebot.types.InlineKeyboardMarkup()
        link = f"tg://user?id={message.from_user.id}"
        button1 = telebot.types.InlineKeyboardButton("user profile", url=link)
        markup.add(button1)
        for address in bot_secrets.GENERALINFOADDRESSEE: # пишем о событии всем желающим
            await bot.send_message(address, 
                f"type:'{message.content_type}'\n"
                f"username: <code>{message.from_user.username}</code>\n"
                f"id: <code>{message.from_user.id}</code>\n" 
#                f" name: {message.from_user.first_name}) "
                f"cleaned in {message.chat.title}, {status=}",
                reply_markup=markup, parse_mode="HTML"
                )
# =========================================================================
# =========================================================================
@bot.message_handler(content_types=["text"])
async def handle_command_message(message: telebot.types.Message) -> None:
    """
    Обработка (удаление + лог) дурацких сообщений о добавленных пользователях
    """
#    print(message)
    if (message.chat.type in ("group", "supergroup")): # обслуживаем только группы
    #обойти все entities и найти bot_command
        delete_this = False
        for entity in message.entities:
            if entity.type == "bot_command":
                delete_this = True
        if(delete_this):
            status = await bot.delete_message(message.chat.id, message.id) #удаляем сообщение
            for address in bot_secrets.GENERALINFOADDRESSEE: # пишем о событии всем желающим
                await bot.send_message(address, 
                    f"command message from username {message.from_user.username} " 
                    f"(id={message.from_user.id}, name={message.from_user.first_name}) "
                    f"deleted in {message.chat.title} with {status=}, "
                    f"text was '{message.text}'"
                    )
# =========================================================================
async def main():
    """
    bot operation
    """
    print("diy little helper started!")
    for address in bot_secrets.GENERALINFOADDRESSEE:
        await bot.send_message(address, "bot started")
    await bot.polling(none_stop=True, interval=5)


# =========================================================================
if __name__ == "__main__":

  asyncio.run(main())
# privet
