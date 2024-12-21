from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

# Ganti dengan token bot Telegram Anda
api_id = '20786693'  # Ganti dengan API ID Anda
api_hash = '6eebbb7d9f9825a2d200c034bfbb7102'  # Ganti dengan API Hash Anda
bot_token = '7559677848:AAEZUWxYlCEXZgcllUDKFztK7TmS2tGs_0o'  # Ganti dengan token bot Anda

app = Client("welcome_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Handler untuk /start
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Website Saat Ini : https://bokep2025.us")

# Handler untuk anggota baru
@app.on_message(filters.new_chat_members)
async def add_group(client, message):
    for member in message.new_chat_members:
        # Membuat tombol dengan link yang diberikan
        keyboard = [
            [InlineKeyboardButton("🔐Buka Kunci Media🔐", url="https://t.me/share/url?text=Asupan+SMA+💦+:+https://t.me/joinchat/7P2DFzD_s5I1MTM1+\n\n+Pemersatu+Bangsa+💦+:+https://t.me/joinchat/vG-iFZLTulg2Zjhl")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Mengirim gambar dengan spoiler dan pesan
        message = await message.reply_photo(
            photo="https://i.ibb.co.com/L8YvcTB/6276011250815189839-120.jpg",  # Ganti dengan URL gambar yang sesuai
            caption=f"👋 Hai {member.full_name}\n\n"
                    "Semua Chat Disembunyikan Untuk Anggota Baru\n"
                    "Anda Harus Membuka Kunci Dengan Cara Bagikan Ke 3 - 5 Grup.\n\n"
                    "Total Media Grup :\n"
                    "📷 Foto = 75683\n"
                    "📹 Video = 27603\n\n"
                    "Cara Buka Kunci Media:\n"
                    "Klik Tombol Buka Kunci Dan Bagikan Ke 3 - 5 Grup Untuk Membuka.\n\n"
                    "Note:\n"
                    "Jika Terverifikasi Anda Sudah Bisa Mengirim Pesan Dan Melihat Video Di Grup Ini.\n"
                    "Jika Anda Keluar Grup Maka Anda Tidak Bisa Bergabung Kembali.",
            reply_markup=reply_markup,
            has_spoiler=True  # Menyembunyikan gambar dengan spoiler
        )

        # Menunggu selama 15 detik dan menghapus pesan
        await asyncio.sleep(15)
        await message.delete()

# Menjalankan bot dan mencetak 'Berhasil' jika berjalan lancar
if __name__ == "__main__":
    print("Berhasil: Bot telah berhasil diinstal dan siap dijalankan.")
    app.run()
