from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import random
from message_api import data   # 🔹 import data dari file message-api.py

# Ganti dengan token bot Telegram Anda
api_id = '20786693'
api_hash = '6eebbb7d9f9825a2d200c034bfbb7102'
bot_token = '7508753099:AAHLs4Xcn7e9N2tXQu9EjGWnAn4efFAMmAs'

app = Client("welcome_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# 🔹 Command /start (kirim random 1 item)
@app.on_message(filters.command("start"))
async def start(client, message):
    item = random.choice(data)  # pilih random 1 data

    keyboard = [
        [InlineKeyboardButton("🔗 Buka Link", url=item["url"])]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await client.send_photo(
        chat_id=message.chat.id,
        photo=item["photo"],
        caption=f"**{item['title']}**\n\nKlik tombol di bawah untuk membuka.",
        reply_markup=reply_markup
    )


@app.on_message(filters.new_chat_members)
async def add_group(client, message):
    for member in message.new_chat_members:
        name = member.first_name
        if member.last_name:
            name += " " + member.last_name

        share_message = (
            "🔥 **Bergabung di Grup Baru :**\n\n"
            "**BokepSenja .com** 💦 : https://t.me/joinchat/j4cRH_jg7VJhN2I1\n\n"
            "**Asupan SMA** 💦 : https://t.me/joinchat/JdpYxovFx3IyMjg1\n\n"
            "**Channel ** 💦 : @BokepSenjaBot\n\n"
            "**Website** : https://bokepsenja.com"
        )

        from urllib.parse import quote
        encoded_message = quote(share_message)

        keyboard = [
            [InlineKeyboardButton("🔐 Buka Kunci Media 🔐", url=f"tg://msg?text={encoded_message}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        sent_message = await client.send_photo(
            chat_id=message.chat.id,
            photo="https://i.ibb.co/L8YvcTB/6276011250815189839-120.jpg",
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

        await asyncio.sleep(30)
        await sent_message.delete()


if __name__ == "__main__":
    print("Berhasil: Bot telah berhasil diinstal dan siap dijalankan.")
    app.run()
