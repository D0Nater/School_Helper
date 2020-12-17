# -*- coding: utf-8 -*-

from config import Main
from keyboard import Keyboard

""" Tasks """
from all_json_data import *
from tasks.admin_panel import AdminPanel


class Command:
    @staticmethod
    def get_answer(chat_id, command):
        if not chat_id in Main.USER_LIST:
            Main.USER_LIST[chat_id] = {"dir": "menu"}

        user_dir = Main.USER_LIST[chat_id]["dir"].split("/")

        try:
            if command in all_commands:
                all_commands[command](chat_id, command)

            elif user_dir[1] in all_lessons[user_dir[0]]["more"]:
                all_lessons[user_dir[0]]["more"][user_dir[1]]["func"](chat_id, command)
        except IndexError:
            pass

    @staticmethod
    def start_command(chat_id, _):
        Main.BOT.send_message(chat_id, "Привет 👋\nЯ бот для помощи в учёбе 🙂\nЧто бы узнать больше, напиши команду /help")

    @staticmethod
    def help_command(chat_id, _):
        Main.BOT.send_message(chat_id, "Это бот для помощи в учёбе. Здесь можно найти разные формулы и решения задач. А главное всегда под рукой 😊\n\nЧто бы открыть меню введите команду /menu")


all_commands = {
    "/start": Command.start_command,
    "/help": Command.help_command,
    "/admin": Keyboard.admin_keyboard,
    "/menu": Keyboard.menu_keyboard
}
