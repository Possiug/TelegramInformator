from telegram import Update, User, Chat, Message
from telegram.ext import ContextTypes, Application, ApplicationBuilder, CommandHandler, MessageHandler
import json
import os
import os.path
from greate_logger import Logger
from classes import *
from decorators import *


LOGGER = Logger('main')
LOGGER.log("Starting...")


def load_cfg() -> Config:
    LOGGER.log("Loading cfg...")
    LOGGER.fin()
    try:
        if (not os.path.exists("config.json")):
            LOGGER.warn("Config doesn't exists, creating new one...")
            with open('config.json', 'w') as fo:
                with open('default_config.json') as fi:
                    fo.write(fi.read())
            raise RuntimeError("Fill config!")
        result: dict | None = None
        with open('config.json') as f:
            result = json.load(f)
        result = Config(result)
        LOGGER.fout()
        LOGGER.info("Config loaded")
        return result
    except Exception as e:
        LOGGER.handle_error(e)
        exit(1)
    

@command_handler
async def start_proc(chat: Chat, user: User, msg: Message, args: list[str]):
    await msg.reply_text(
        "Wellcome!\nЭто бот для поиска публичной информации о человеке по его телеграм профилю!\n" \
        "Чтобы найти информацию отправьте username, номер телефона или поделитесь чатом/пользователем\n\n" \
        "Бот разработан: @possiug\n<a href=\"https://github.com/Possiug/TelegramInformator\">Исходный код</a>", 'HTML'
    )


def main():
    config = load_cfg()
    try: 
        application = ApplicationBuilder().token(config.tg_token).build()


        LOGGER.log("Register handlers")
        application.add_handler(CommandHandler("start", start_proc))
        LOGGER.info("Bot running...")
        application.run_polling()
    except Exception as e:
        LOGGER.handle_error(e)

    

if __name__ == '__main__':
    main()






