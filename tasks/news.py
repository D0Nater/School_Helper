# -*- coding: utf-8 -*-

from config import Main


class News:
    def write_news(chat_id):
        user_dir = Main.USER_LIST[chat_id]["dir"].split("/")

        if "bot_v" in user_dir:
            Main.BOT.send_message(chat_id, f"Версия бота: v{Main.VERSION}")
            return

        elif "bot_news" in user_dir:
            Main.BOT.send_message(chat_id, "Новое %s" % ("\n".join(Main.NEWS)))
            return


all_news = {
    "bot_v": {
        "text": "Версия бота",
        "func": News.write_news
    },
    "bot_news": {
        "text": "Новое",
        "func": News.write_news
    }
}
