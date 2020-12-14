# -*- coding: utf-8 -*-

from config import Main


class Rule:
    def write_text(f_dir, file):
        with open(f"{f_dir}/{file}") as f:
            Main.BOT.send_message(chat_id=chat_id, text=f.read())


rus_rules = {}

eng_rules = {}

math_rules = {
    # Abbreviated multiplication formulas
    "AMF": {
        "text": "Формулы сокращенного умножения",
        "file": "AMF.txt"
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
