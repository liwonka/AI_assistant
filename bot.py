from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from docx import Document

# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ИИ-ассистент сделанный командой Миньоны для хакатона')

# Обработка документов
def handle_document(update: Update, context: CallbackContext) -> None:
    file = update.message.document.get_file()
    file.download('received_file.docx')

    # Отправляем пустой документ обратно пользователю
    with open('empty_file.docx', 'rb') as f:
        update.message.reply_document(document=InputFile(f, filename='empty_file.docx'))

def echo(update: Update, context: CallbackContext) -> None:
    first_name = str(update.message.from_user.first_name)
    last_name = str(update.message.from_user.last_name)
    update.message.reply_text("Отвечаю обратно пользователю " + first_name + " " + last_name)

# Основная функция
def main() -> None:
    # Вставьте сюда ваш токен
    TOKEN = '7381756413:AAECp5pgevxJaKQCi3s4gi5cHLZD-JhEKkI'

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(
        Filters.document.mime_type("application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
        handle_document))
    #dispatcher.add_handler(MessageHandler(Filters.document.mime_type("application/msword"), handle_document))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    # Запускаем бота
    updater.start_polling()

    # Ожидаем завершения работы
    updater.idle()


if __name__ == '__main__':
    main()
