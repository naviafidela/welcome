import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

# Ganti dengan token yang sesuai jika Anda tidak menggunakan variabel lingkungan
TOKEN = "7559677848:AAEZUWxYlCEXZgcllUDKFztK7TmS2tGs_0o"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('''𝙷𝚊𝚒 , \n\n𝙸𝚊𝚖 𝚊 𝚂𝚒𝚖𝚙𝚕𝚎 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝙱𝚘𝚝. 𝙰𝚍𝚍 𝚖𝚎 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙 𝚊𝚗𝚍 𝚖𝚊𝚔𝚎 𝚖𝚎 𝚊𝚜 𝚊𝚍𝚖𝚒𝚗\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍 𝙱𝚢 : @BX_Botz ''')

async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("➠ 𝙰𝚍𝚍 𝙼𝚎 𝚃𝚘 𝙶𝚛𝚘𝚞𝚙\n\n➠ 𝙼𝚊𝚔𝚎 𝙰𝚍𝚖𝚒𝚗 𝙼𝚎\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍 𝙱𝚢 : @BX_Botz")

async def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        # Membuat tombol dengan link yang diberikan
        keyboard = [
            [InlineKeyboardButton("🔐Buka Kunci Media🔐", url="https://t.me/share/url?text=Asupan+SMA+💦+:+https://t.me/joinchat/7P2DFzD_s5I1MTM1+\n\n+Pemersatu+Bangsa+💦+:+https://t.me/joinchat/vG-iFZLTulg2Zjhl")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Mengirim gambar sebagai spoiler
        message = await update.message.bot.send_photo(
            chat_id=update.message.chat_id,
            photo="https://i.ibb.co/com/L8YvcTB/6276011250815189839-120.jpg",  # URL gambar
            caption=f"Hai {member.full_name}\n\n"
                    "Semua Chat Disembunyikan Untuk Anggota Baru\n"
                    "Anda Harus Membuka Kunci Dengan Cara Bagikan Ke 3 - 5 Grup.\n\n"
                    "Total Media Grup :\n"
                    "📷Foto = 75683\n"
                    "📹Video = 27603\n\n"
                    "Cara Buka Kunci Media:\n"
                    "Klik Tombol Buka Kunci Dan Bagikan Ke 3 - 5 Grup Untuk Membuka.\n\n"
                    "Note: Jika Terverifikasi Anda Sudah Bisa Mengirim Pesan Dan Melihat Video Di Grup Ini. Jika Anda Keluar Grup Maka Anda Tidak Bisa Bergabung Kembali.",
            reply_markup=reply_markup,
            spoiler=True  # Menyembunyikan gambar dengan spoiler
        )

        # Menjadwalkan penghapusan pesan setelah 15 detik
        await context.job_queue.run_once(delete_message, 15, context=message)

async def delete_message(context: CallbackContext):
    # Menghapus pesan setelah 15 detik
    message = context.job.context
    await context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)

# Inisialisasi Application dan bot
application = Application.builder().token(TOKEN).build()

# Menambahkan handler untuk start dan help
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help))

# Menambahkan handler untuk anggota baru
application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, add_group))

# Mulai polling
if __name__ == '__main__':
    print("Sukses: Bot telah berhasil diinstal dan siap dijalankan.")
    application.run_polling()
