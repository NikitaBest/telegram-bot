from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Вставьте ваш токен от BotFather
TOKEN = "7136327097:AAFGcc98LpfsoYJ6o-aagp3-I6k0iJDVdRU"

# Функция приветствия с меню кнопок
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user  # Получаем данные пользователя
    # Создаем клавиатуру с кнопками
    keyboard = [
        ['Работа в банке', 'Подработка'],
        ['Обучение', 'Микрозаймы']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Отправляем приветственное сообщение
    await update.message.reply_text(
        f"Привет, {user.first_name}! Добро пожаловать! Выберите, что вас интересует:",
        reply_markup=reply_markup
    )

# Обработка нажатий на кнопки
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text  # Получаем текст нажатой кнопки

    # Обрабатываем каждую кнопку
    if text == "Работа в банке":
        await update.message.reply_text("Информация о работе в банке:\nВакансии доступны на нашем сайте.")
    elif text == "Подработка":
        await update.message.reply_text("Подработка доступна в вечерние и выходные часы. Напишите нам для подробностей.")
    elif text == "Обучение":
        await update.message.reply_text("Мы предлагаем курсы по программированию, дизайну и маркетингу. Выберите курс на сайте.")
    elif text == "Микрозаймы":
        await update.message.reply_text("Условия микрозаймов:\nСуммы от 5 000 до 50 000 рублей. Срок возврата до 30 дней.")
    else:
        await update.message.reply_text("Пожалуйста, выберите опцию из меню.")

# Основная функция запуска бота
def main():
    # Создаем экземпляр приложения
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_button))

    # Запускаем бота
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    application.run_polling()

# Запускаем код, если файл выполняется напрямую
if __name__ == "__main__":
    main()

