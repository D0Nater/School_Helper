# -*- coding: utf-8 -*-

import telebot


class Main:
    ADMINS = []

    START_TIME = ""

    TOKEN = ""

    BOT = telebot.TeleBot(TOKEN)

    USER_LIST = {}
