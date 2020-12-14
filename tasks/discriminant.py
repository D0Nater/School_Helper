# -*- coding: utf-8 -*-

from math import sqrt

from config import Main


class Discriminant:
    @staticmethod
    def get_chat_id(chat_id, text=""):
        if Main.USER_LIST[chat_id]["dir"].split("/")[-1] == "set_nums":
            Discriminant().set_nums(chat_id, text)
            return

        Main.USER_LIST[chat_id]["dir"] += "/set_nums"

        Main.BOT.send_message(chat_id, "Решение Дискриминанта\n\nНапишите сообщение такого типа: a b c - (разделяя пробелом):\n1 3 -4")

    def set_nums(self, chat_id, text):
        def write_example():
            def num_to_str(num, x=False):
                if num > 0:
                    return f" + {num}" + ("x" if x else "")
                elif num < 0:
                    return " - %s" % (str(num).replace("-", "")) + ("x" if x else "")
                return ""

            return "%sx²%s%s = 0" % (self.a_num, num_to_str(self.b_num, x=True), num_to_str(self.c_num))

        def write_discriminant():
            def num_to_str(num):
                if num > 0:
                    return num
                elif num < 0:
                    return f"({num})"
                return ""

            def solve_discriminant():
                def num_to_str(num):
                    if num > 0:
                        return f" + {num}"
                    elif num < 0:
                        return " - %.2f" % float(str(num).replace("-", ""))
                    return ""

                discr1 = "%.2f" % self.b_num ** 2
                discr2 = num_to_str(- 4 * self.a_num * self.c_num)
                discr3 = "%.2f" % (self.b_num ** 2 - 4 * self.a_num * self.c_num)

                return [f"{discr1}{discr2} = {discr3}", float(discr3)]

            discr = solve_discriminant()

            answ = "D = b² - 4ac\n"
            answ += "D = %s² - 4 * %s * %s = %s" % (
                self.b_num,
                num_to_str(self.a_num),
                num_to_str(self.c_num),
                discr[0]
            )

            return [answ, discr[1]]


        self.answer_text = ""

        self.text = text.replace(",", ".").split(" ")

        try:
            self.a_num = float(self.text[0])
            self.b_num = float(self.text[1])
            self.c_num = float(self.text[2])
        except:
            Main.BOT.send_message(chat_id, "Ошибка. Прочитайте как правильно писать сообщение")
            return

        self.discr = write_discriminant()
        self.answer_text += write_example()
        self.answer_text += "\n\n" + self.discr[0]

        if self.discr[1] > 0:
            self.x1 = (-self.b_num + sqrt(self.discr[1])) / (2 * self.a_num)
            self.x2 = (-self.b_num - sqrt(self.discr[1])) / (2 * self.a_num)
            self.answer_text += "\n\nx = -b±√D / 2a"
            self.answer_text += "\nx = -%s±√%s / 2*%s" % (self.b_num, self.discr[1], self.a_num)
            self.answer_text += "\n\nx1 = %.2f \nx2 = %.2f" % (self.x1, self.x2)

        elif self.discr[1] == 0:
            self.x = -self.b_num / (2 * self.a_num)
            self.answer_text += "\n\nx = -b / 2a"
            self.answer_text += "\nx = -%s / 2*%s" % (self.b_num, self.a_num)
            self.answer_text += "\n\nx = %.2f" % self.x

        else:
            self.answer_text += "\n\nКорней Нет!"

        Main.BOT.send_message(chat_id, self.answer_text)
