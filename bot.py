from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import asyncio
import random
from message_api import data   # 🔹 data dari message-api.py

import aiohttp
from io import BytesIO
from PIL import Image


# Ganti dengan token bot Telegram Anda
api_id = '20786693'
api_hash = '6eebbb7d9f9825a2d200c034bfbb7102'
bot_token = '7508753099:AAHLs4Xcn7e9N2tXQu9EjGWnAn4efFAMmAs'

app = Client("welcome_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


# 🔹 Fungsi fetch & resize ke 16:9
async def fetch_and_resize(url, width=1280, height=720):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            img_bytes = await resp.read()

    img = Image.open(BytesIO(img_bytes))
    img = img.convert("RGB")

    # Crop cover tengah biar tidak gepeng
    img_ratio = img.width / img.height
    target_ratio = width / height

    if img_ratio > target_ratio:
        # crop kiri-kanan
        new_width = int(img.height * target_ratio)
        offset = (img.width - new_width) // 2
        img = img.crop((offset, 0, offset + new_width, img.height))
    else:
        # crop atas-bawah
        new_height = int(img.width / target_ratio)
        offset = (img.height - new_height) // 2
        img = img.crop((0, offset, img.width, offset + new_height))

    img = img.resize((width, height), Image.LANCZOS)

    output = BytesIO()
    output.name = "image.jpg"
    img.save(output, format="JPEG", quality=90)
    output.seek(0)
    return output


# 🔹 Generate keyboard
def build_keyboard(item):
    keyboard = [
        [InlineKeyboardButton("🔥BUKA LINK VIDEO🔥", url=item["url"])],
        [
            InlineKeyboardButton("🗪GRUP 1", url="https://t.me/joinchat/j4cRH_jg7VJhN2I1"),
            InlineKeyboardButton("🗪GRUP 2", url="https://t.me/joinchat/JdpYxovFx3IyMjg1")
        ],
        [InlineKeyboardButton("📢Join Channel", url="https://t.me/BokepSenjaBot")],
        [InlineKeyboardButton("🔄Cari Video Lainnya", callback_data="next")]
    ]
    return InlineKeyboardMarkup(keyboard)


# 🔹 Command /start
@app.on_message(filters.command("start"))
async def start(client, message):
    item = random.choice(data)
    resized_photo = await fetch_and_resize(item["photo"], 1280, 720)

    reply_markup = build_keyboard(item)

    await client.send_photo(
        chat_id=message.chat.id,
        photo=resized_photo,
        caption=f"**{item['title']}**\n\nKlik tombol di bawah untuk membuka.",
        reply_markup=reply_markup
    )


# 🔹 Callback untuk "Cari Video Lainnya"
@app.on_callback_query()
async def callback_handler(client, callback_query):
    if callback_query.data == "next":
        item = random.choice(data)
        resized_photo = await fetch_and_resize(item["photo"], 1280, 720)
        reply_markup = build_keyboard(item)

        await callback_query.message.edit_media(
            media=InputMediaPhoto(resized_photo, caption=f"**{item['title']}**\n\nKlik tombol di bawah untuk membuka."),
            reply_markup=reply_markup
        )

        await callback_query.answer()


# 🔹 Event saat ada member baru masuk grup
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


# 🔹 Run bot
if __name__ == "__main__":
    print("Berhasil: Bot telah berhasil diinstal dan siap dijalankan.")
    app.run()
