import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

# Ganti dengan token yang sesuai jika Anda tidak menggunakan variabel lingkungan
TOKEN = "7559677848:AAEZUWxYlCEXZgcllUDKFztK7TmS2tGs_0o"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('''𝙷𝚊𝚒 , \n\n𝙸𝚊𝚖 𝚊 𝚂𝚒𝚖𝚙𝚕𝚎 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝙱𝚘𝚝. 𝙰𝚍𝚍 𝚖𝚎 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙 𝚊𝚗𝚍 𝚖𝚊𝚔𝚎 𝚖𝚎 𝚊𝚜 𝚊𝚍𝚖𝚒𝚗\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍 𝙱𝚢 : @BX_Botz ''')

async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("➠ 𝙰𝚍𝚍 𝙼𝚎 𝚃𝚘 𝙶𝚛𝚘𝚞𝚙\n\n➠ 𝙼𝚊𝚔𝚎 𝙰𝚍𝚖𝚒𝚗 𝙼𝚎\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍 𝙱𝚢 : @BX_Botz")

async def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f'Hai {member.full_name} , Welcome to ln Support\n\n💖Thank💖You💖For💖Joining💖')

# Inisialisasi Application dan bot
application = Application.builder().token(TOKEN).build()

# Menambahkan handler untuk start dan help
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help))

# Menambahkan handler untuk anggota baru
application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, add_group))

# Mulai polling
if __name__ == '__main__':
    application.run_polling()
