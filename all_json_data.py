# -*- coding: utf-8 -*-

from tasks.news import *
from tasks.rules import *
from tasks.admin_panel import AdminPanel

from tasks.discriminant import Discriminant
from tasks.arc_progress import ArithmeticProgression


math_more = {
    "discr": {
        "text": "Дискриминант",
        "func": Discriminant.get_chat_id
    },
    "arc_progr": {
        "text": "Арифметическая прогрессия",
        "func": ArithmeticProgression.get_chat_id
    }
}

geom_more = {}


all_lessons = {
    "news": {
        "text": "Новости 📰",
        "more": all_news
    },
    "rules": {
        "text": "Правила/Теоремы 📚",
        "more": all_rules
    },
    "math": {
        "text": "Алгебра 🧮",
        "more": math_more
    },
    "geom": {
        "text": "Геометрия 📐",
        "more": geom_more
    }
}


admin_commands = {
    "Старт бота": AdminPanel.bot_start_time,
    "Пользователи": AdminPanel.print_users
}
