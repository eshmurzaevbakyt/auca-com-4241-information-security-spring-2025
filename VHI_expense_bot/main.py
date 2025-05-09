from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from expenses import add_expense_programmatically

TOKEN = "7480527089:AAFhIvVgwUiSvdERK0SkLxwgy19g6TR3ndI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь /add <описание> <сумма> <дата>, чтобы сохранить расход.")

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        _, category, amount, date = update.message.text.split(" ", 3)
        add_expense_programmatically(date, category, float(amount), method="telegram")
        await update.message.reply_text("Расход добавлен!")
    except Exception as e:
        await update.message.reply_text(
            "Ошибка. Используй: /add категория сумма дата\n"
            "например: /add Анализ 1500 2024-05-10"
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))

    print("Бот запущен...")
    app.run_polling()
