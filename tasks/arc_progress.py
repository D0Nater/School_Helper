# -*- coding: utf-8 -*-

from config import *


class ArithmeticProgression:
    @staticmethod
    def get_chat_id(chat_id, text=""):
        user_dir = Main.USER_LIST[chat_id]["dir"].split("/")

        if "search_an" in user_dir:
            ArithmeticProgression.get_search_an(chat_id, text, user_dir)
            return

        elif "arc_sum" in user_dir:
            ArithmeticProgression.get_arc_sum(chat_id, text, user_dir)
            return

        markup = telebot.types.InlineKeyboardMarkup()

        markup.add(telebot.types.InlineKeyboardButton(text="⬅️ Назад", callback_data="math"))

        markup.add(telebot.types.InlineKeyboardButton(text="Найти a_n", callback_data="math/arc_progr/search_an"))
        markup.add(telebot.types.InlineKeyboardButton(text="Сумма", callback_data="math/arc_progr/arc_sum"))

        Main.BOT.send_message(chat_id, "Арифметическая прогрессия", reply_markup=markup)

    @staticmethod
    def get_search_an(chat_id, text="", user_dir=[]):
        if "get_search_an" in user_dir:
            ArithmeticProgression().search_an(chat_id, text)
            return

        Main.BOT.send_message(chat_id, "Нахождение a_n\n\nНапишите сообщение такого типа: a1 d n - (разделяя пробелом, где a1 — первый член прогрессии, d — разность прогрессии, n — номер для нахождения):\n3 2 5")

        Main.USER_LIST[chat_id]["dir"] += "/get_search_an"

    @staticmethod
    def get_arc_sum(chat_id, text="", user_dir=[]):
        if "get_arc_sum" in user_dir:
            ArithmeticProgression().arc_sum(chat_id, text)
            return

        Main.BOT.send_message(chat_id, "Нахождение суммы арифметической прогрессии\n\nНапишите сообщение такого типа: a1 a_n n - (разделяя пробелом, где a1 — первый член прогрессии, a_n  — последний член, n  — количество членов в данной прогрессии):\n3 30 10")

        Main.USER_LIST[chat_id]["dir"] += "/get_arc_sum"

    def search_an(self, chat_id, text=""):
        def num_to_str(num):
            if num > 0:
                return f" + {num}"
            elif num < 0:
                return " - %.2f" % float(str(num).replace("-", ""))
            return ""

        def solve_a_n(a1, d, n):
            return a1 + d*(n-1) 

        self.answer_text = "Формула нахождения a_n:\na_n = a1+d(n-1)"
        self.text = text.split(" ")

        try:
            self.a1_num = float(self.text[0])
            self.d_num = float(self.text[1])
            self.n_num = int(self.text[2])
        except:
            Main.BOT.send_message(chat_id, "Ошибка. Прочитайте как правильно писать сообщение")
            return

        self.answer_text += "\n\na_n = %s%s(%s-1)" % (self.a1_num, num_to_str(self.d_num), self.n_num)
        self.answer_text += "\na_n = %s%s" % (self.a1_num, num_to_str(self.d_num*(self.n_num-1)))
        self.answer_text += "\na_n = %s" % (solve_a_n(self.a1_num, self.d_num, self.n_num))

        Main.BOT.send_message(chat_id, self.answer_text)

    def arc_sum(self, chat_id, text=""):
        def num_to_str(num):
            if num > 0:
                return f" + {num}"
            elif num < 0:
                return " - %.2f" % float(str(num).replace("-", ""))
            return ""

        self.answer_text = "Формула сумма членов арифметической прогрессии:\nS = (a1 + a_n)n / 2"
        self.text = text.split(" ")

        try:
            self.a1_num = float(self.text[0])
            self.a_n_num = float(self.text[1])
            self.n_num = int(self.text[2])
        except:
            Main.BOT.send_message(chat_id, "Ошибка. Прочитайте как правильно писать сообщение")
            return

        answ1 = (self.a1_num + self.a_n_num)*self.n_num

        self.answer_text += "\n\nS = (%s%s)*%s / 2" % (self.a1_num, num_to_str(self.a_n_num), self.n_num)
        self.answer_text += "\nS = %s / 2" % (answ1)
        self.answer_text += "\nS = %s" % (answ1/2)

        Main.BOT.send_message(chat_id, self.answer_text)
