from telegram import Update, User, Chat, Message, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestUsers, ReplyKeyboardRemove
from telegram.ext import ContextTypes, Application, ApplicationBuilder, CommandHandler, MessageHandler, filters
import json
import os
import os.path
from greate_logger import Logger
from classes import *
from decorators import *


LOGGER = Logger('main', True)
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
        "Wellcome!\nЭто бот для поиска <b>публичной</b> информации о человеке по его телеграм профилю!\n" \
        "Чтобы найти информацию отправьте username, номер телефона или поделитесь чатом/пользователем\n\nИспользуйте /me чтобы настроить аккаунт\n\n" \
        "Бот разработан: @possiug\n<a href=\"https://github.com/Possiug/TelegramInformator\">Исходный код</a>", 'HTML', reply_markup=ReplyKeyboardRemove()
    )


async def msg_proc(u: Update, c: ContextTypes.DEFAULT_TYPE):
    msg = u.effective_message
    if (msg.text.startswith('@')):
        LOGGER.info("collect info by username")
    elif (msg.text.startswith('+')):
        LOGGER.info("collect info by phone")
    else:
        rpmk = ReplyKeyboardMarkup(
            [
                [KeyboardButton("User", request_users=KeyboardButtonRequestUsers(166, False, request_username=True))]
            ],
            True,
            True
        )
        await msg.reply_text("Необходимо отправить одну из следующих вещей:\n" \
        "1) Имя пользователя в формате: @username\n2) Телефон в формате: +номертелефона", "HTML", reply_markup=rpmk)


async def error_proc(u: Update, c: ContextTypes.DEFAULT_TYPE):
    LOGGER.error(f"chat: {u.effective_chat.id} user[{u.effective_user.username}] msg: {u.effective_message.text}")
    LOGGER.handle_error(c.error)
    try:
        await u.effective_chat.send_message("Произошла непредвиденная ошибка!\nСообщите разработчику (@possiug)", "HTML")
    except Exception as e:
        LOGGER.warn("Failed to inform an user about error!")


def main():
    config = load_cfg()
    try: 
        application = ApplicationBuilder().token(config.tg_token).build()


        LOGGER.log("Register handlers")
        application.add_error_handler(error_proc, False)
        application.add_handler(CommandHandler("start", start_proc))
        application.add_handler(MessageHandler(filters.TEXT, msg_proc, False))
        LOGGER.info("Bot running...")
        application.run_polling()
    except Exception as e:
        LOGGER.handle_error(e)

    

if __name__ == '__main__':
    main()






