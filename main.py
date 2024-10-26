import asyncio

import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

nest_asyncio.apply()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_chat.type == 'private':
        chat_id = update.effective_chat.id

        await context.bot.send_sticker(chat_id=chat_id, sticker='CAACAgIAAxkBAAENA5NnHCa3BUAc_ZbZrm5F2tbotfuBHQACrFAAAhvEOErgakBPSL5PRTYE')
        await context.bot.send_message(chat_id=chat_id, text='*Я не владею функциями в ЛС!\nПрисоединяйся к @null_dev*', parse_mode='MarkdownV2')


async def main() -> None:
    application = ApplicationBuilder().token('7804030886:AAFmqYAPW08gRlS6N6ASwqp5GXNPyifcS64').build()

    application.add_handler(CommandHandler('start', start))

    await application.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
