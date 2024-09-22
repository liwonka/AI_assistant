from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from docx import Document

# Команда /start
# Команда /start
'''def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Здравствуйте! Отправьте мне файл своей НИР или ВКР, и я исправлю его в соответствии с ГОСТ.')

# Обработка документов
def handle_document(update: Update, context: CallbackContext) -> None:
    file = update.message.document.get_file()
    file.download('received_file.docx')

    # Создаем пустой документ
    doc = Document()
    doc.save('отчет.docx')

    # Отправляем пустой документ обратно пользователю
    with open('отчет.docx', 'rb') as f:
        update.message.reply_text("Готово! Все замечания и правки по работе я отразил в отчете")
        update.message.reply_document(document=InputFile(f, filename='отчет.docx'))

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Это не .doc/.docx файл!')

# Основная функция
def main() -> None:
    # Вставьте сюда ваш токен
    TOKEN = '7381756413:AAECp5pgevxJaKQCi3s4gi5cHLZD-JhEKkI'

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(
        filters.document.mime_type("application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
        handle_document))
    dispatcher.add_handler(MessageHandler(filters.document.mime_type("application/msword"), handle_document))

    dispatcher.add_handler(MessageHandler(filters.text, echo))
    # Запускаем бота
    updater.start_polling()

    # Ожидаем завершения работы
    updater.idle()


if __name__ == '__main__':
    main()



import telebot
from telebot import types

bot = telebot.TeleBot('7381756413:AAECp5pgevxJaKQCi3s4gi5cHLZD-JhEKkI')

@bot.message_handler(content_types=['document'])
def handle_document(message):
    if message.document.mime_type in ['application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        with open('received_file.docx', 'wb') as f:
            f.write(downloaded_file)

        bot.send_document(message.chat.id, open('received_file.docx', 'rb'))
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, отправьте файл в формате .doc или .docx.')

bot.polling()
'''





import telebot
from telebot import types

bot = telebot.TeleBot('7381756413:AAECp5pgevxJaKQCi3s4gi5cHLZD-JhEKkI')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'На связи AI ассистент!')

@bot.message_handler(content_types=['document', 'text'])
def handle_input(message):
    if message.content_type == 'document':
        if message.document.mime_type in ['application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            with open('received_file.docx', 'wb') as f:
                f.write(downloaded_file)

            bot.send_document(message.chat.id, open('received_file.docx', 'rb'))
        else:
            bot.send_message(message.chat.id, 'Это не .doc/.docx!')
    else:
        bot.send_message(message.chat.id, 'Это не .doc/.docx!')

bot.polling()
