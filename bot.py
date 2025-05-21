from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

# Ganti dengan token bot Telegram Anda
api_id = '20786693'  # Ganti dengan API ID Anda
api_hash = '6eebbb7d9f9825a2d200c034bfbb7102'  # Ganti dengan API Hash Anda
bot_token = '7508753099:AAEAOAVefdjLDSKCQSTPJM2p1bmUMhV5V9Y'  # Ganti dengan token bot Anda

app = Client("welcome_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.new_chat_members)
async def add_group(client, message):
    for member in message.new_chat_members:
        # Membuat nama lengkap dari member
        name = member.first_name
        if member.last_name:
            name += " " + member.last_name

        # Membuat tombol dengan link untuk berbagi pesan
        share_message = (
            "🔥 **Bergabung di Grup Baru :**\n\n"
            "**BokepSenja .com** 💦 : https://t.me/joinchat/j4cRH_jg7VJhN2I1\n\n"
            "**Asupan SMA** 💦 : https://t.me/joinchat/JdpYxovFx3IyMjg1\n\n"
            "**Channel ** 💦 : @BokepSenjaBot\n\n"
            "**Website** : https://bokepsenja.com"
        )

        # Encode message untuk URL
        from urllib.parse import quote
        encoded_message = quote(share_message)

        # Membuat tombol dengan URL untuk berbagi
        keyboard = [
            [InlineKeyboardButton("🔐 Buka Kunci Media 🔐", url=f"tg://msg?text={encoded_message}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Mengirim gambar dengan spoiler dan pesan
        sent_message = await client.send_photo(
            chat_id=message.chat.id,  # Mengirim ke grup yang sama
            photo="https://i.ibb.co/L8YvcTB/6276011250815189839-120.jpg",  # Ganti dengan URL gambar yang sesuai
            caption=f"👋 Hai {name}\n\n"
                    "Semua Chat Disembunyikan Untuk Anggota Baru\n"
                    "Anda Harus Membuka Kunci Dengan Cara Bagikan Ke 3 - 5 Grup.\n\n"
                    "Total Media Grup :\n"
                    "📷 Foto = 75683\n"
                    "📹 Video = 27603\n\n"
                    "Cara Buka Kunci Media:\n"
                    "Klik Tombol Buka Kunci Dan Bagikan Ke 3 - 5 Grup Untuk Membuka.\n\n"
                    "Note:\n"
                    "Jika Terverifikasi Anda Sudah Bisa Mengirim Pesan Dan Melihat Video Di Grup Ini.\n",
            reply_markup=reply_markup,
            has_spoiler=True
        )

        # Menunggu selama 30 detik dan menghapus pesan
        await asyncio.sleep(30)
        await sent_message.delete()

# Menjalankan bot dan mencetak 'Berhasil' jika berjalan lancar
if __name__ == "__main__":
    print("Berhasil: Bot telah berhasil diinstal dan siap dijalankan.")
    app.run()
