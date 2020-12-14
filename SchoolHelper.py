# -*- coding: utf-8 -*-

# import telebot
from datetime import datetime

from config import *
from commands import Command
from keyboard import Keyboard

from all_json_data import *


@Main.BOT.message_handler(content_types=["text"])
def get_message(message):
    print("%s : %s : %s" % (datetime.now(), message.chat.id, message.text))
    Command.get_answer(message.chat.id, message.text)


@Main.BOT.callback_query_handler(func=lambda call: True)
def query_handler(call):
    chat_id = call.message.chat.id
    call_data = call.data.split("/")

    print("%s : %s : %s" % (datetime.now(), chat_id, call_data))

    if not chat_id in Main.USER_LIST:
        Main.USER_LIST[chat_id] = {"dir": "menu"}

    try:
        if call_data[0] == "menu":
            Keyboard.menu_keyboard(chat_id, None, call.message.message_id)

        elif call_data[0] == "admin":
            admin_commands[call_data[1]](chat_id)

        elif call_data[0] in all_lessons and len(call_data) == 1:
            Keyboard.lesson_keyboard(chat_id, call_data[0], call.message.message_id)

        elif call_data[1] in all_lessons[call_data[0]]["more"]:
            Main.USER_LIST[chat_id]["dir"] = "/".join(call_data)
            all_lessons[call_data[0]]["more"][call_data[1]]["func"](chat_id)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    Main.START_TIME = datetime.now()
    Main.BOT.polling(none_stop=True)
