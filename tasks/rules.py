# -*- coding: utf-8 -*-

from os import path

from config import Main


class Rule:
    def send_file(self, chat_id, json_dir_name):
        self.dir_name = "rules/" + json_dir_name[1] + "/"
        self.file_name = json_dir_name[2] + ".pdf"

        self.file_all = self.dir_name + self.file_name

        if not path.exists(self.file_all):
            Main.BOT.send_message(chat_id, "Dir : %s\nError 404 : file \"%s\" not found.\nСообщите об ошибке администратору!" % (json_dir_name, self.file_all))
            return

        self.file = open(self.file_all, 'rb')
        Main.BOT.send_document(chat_id, self.file)
        self.file.close()


rus_rules = {}

eng_rules = {}

math_rules = {
    "AMF": {
        "text": "Формулы сокращенного умножения"
    },
    "QuadraticEquation": {
        "text": "Квадратное уравнение"
    },
    "APR": {
        "text": "Арифметическая прогрессия"
    },
    "GPR": {
        "text": "Геометрическая прогрессия"
    }
}

geom_rules = {}


all_rules = {
    "rus": {
        "text": "Русский язык",
        "more": rus_rules
    },
    "eng": {
        "text": "Английский язык",
        "more": eng_rules
    },
    "math": {
        "text": "Алгебра",
        "more": math_rules
    },
    "geom": {
        "text": "Геометрия",
        "more": geom_rules
    }
}
