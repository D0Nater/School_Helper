# -*- coding: utf-8 -*-

from config import *

from all_json_data import *


class Keyboard:
    @staticmethod
    def menu_keyboard(chat_id, _, msg_id=None):
        markup = telebot.types.InlineKeyboardMarkup()

        for lesson in all_lessons:
            markup.add(telebot.types.InlineKeyboardButton(text=all_lessons[lesson]["text"], callback_data=lesson))

        if msg_id:
            Main.BOT.edit_message_text(chat_id=chat_id, message_id=msg_id, text="Меню", reply_markup=markup)
        else:
            Main.BOT.send_message(chat_id=chat_id, text="Меню", reply_markup=markup)
        Main.USER_LIST[chat_id]["dir"] = "menu"

    @staticmethod
    def lesson_keyboard(chat_id, json_dir_name, msg_id):
        markup = telebot.types.InlineKeyboardMarkup()

        markup.add(telebot.types.InlineKeyboardButton(text="⬅️ Назад", callback_data="menu"))

        for example in all_lessons[json_dir_name]["more"]:
            example_json = all_lessons[json_dir_name]["more"][example]
            markup.add(telebot.types.InlineKeyboardButton(text=example_json["text"], callback_data=f"{json_dir_name}/{example}"))

        Main.BOT.edit_message_text(chat_id=chat_id, message_id=msg_id, text=all_lessons[json_dir_name]["text"], reply_markup=markup)
        Main.USER_LIST[chat_id]["dir"] = json_dir_name

    @staticmethod
    def admin_keyboard(chat_id, _):
        if not chat_id in Main.ADMINS:
            return

        markup = telebot.types.InlineKeyboardMarkup()

        markup.add(telebot.types.InlineKeyboardButton(text="⬅️ Назад", callback_data="menu"))

        for command in admin_commands:
            markup.add(telebot.types.InlineKeyboardButton(text=command, callback_data=f"admin/{command}"))

        Main.BOT.send_message(chat_id=chat_id, text="Панель Администратора", reply_markup=markup)
        Main.USER_LIST[chat_id]["dir"] = "admin"
