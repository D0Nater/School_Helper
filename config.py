# -*- coding: utf-8 -*-

import telebot


class Main:
    ADMINS = [] # your

    VERSION = "0.1"

    START_TIME = ""

    TOKEN = "" # bot token

    BOT = telebot.TeleBot(TOKEN)

    BAN_LIST = []
    USER_LIST = {}

    NEWS =  "за 14.12.2020", \
            "\nСтарт проекта School Helper.", \
            "\nС каждым днем количество правил, теорем, а так же решений будет расти!", \
            "Следите за самыми свежими новостями и оставайтесь в курсе событий!"
