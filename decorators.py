
from telegram import Update, User, Chat, Message
from telegram.ext import ContextTypes, Application, ApplicationBuilder, CommandHandler, MessageHandler


def command_handler(func):
    async def wrapper(u: Update, c: ContextTypes.DEFAULT_TYPE):
        await func(u.effective_chat, u.effective_user, u.effective_message, c.args)
    return wrapper