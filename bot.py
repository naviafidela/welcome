from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

API_TOKEN = 'YOUR_API_TOKEN'

async def welcome_message(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        print(f"Anggota baru: {member.first_name}")  # Pastikan log muncul
        await update.message.reply_text(f"Selamat datang, {member.first_name}! 🎉")

# Inisialisasi aplikasi
application = Application.builder().token(API_TOKEN).build()

# Tambahkan handler untuk anggota baru
welcome_handler = MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_message)
application.add_handler(welcome_handler)

if __name__ == '__main__':
    application.run_polling()
