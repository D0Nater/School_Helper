# -*- coding: utf-8 -*-

import telebot

from config import Main


class AdminPanel:
    @staticmethod
    def print_users(chat_id):
        Main.BOT.send_message(chat_id, text=Main.USER_LIST.keys())

    @staticmethod
    def bot_start_time(chat_id):
        Main.BOT.send_message(chat_id, text=Main.START_TIME)
