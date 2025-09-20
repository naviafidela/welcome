from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import asyncio
import random
import aiohttp
from io import BytesIO
from PIL import Image

# === CONFIG ===
API_URL = "https://bokepsenja.com/api/TelegramDataVideoWelcome.php"  # ganti dengan URL index.php kamu
api_id = '20786693'
api_hash = '6eebbb7d9f9825a2d200c034bfbb7102'
bot_token = '7508753099:AAHLs4Xcn7e9N2tXQu9EjGWnAn4efFAMmAs'

app = Client("welcome_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# === Fetch data dari API ===
async def get_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as resp:
            if resp.status != 200:
                return []
            return await resp.json()

async def get_random_item():
    data = await get_data()
    if not data:
        return None
    return random.choice(data)
    
# === Keyboard ===
def build_keyboard(item):
    keyboard = [
        [InlineKeyboardButton("🔥 BUKA LINK VIDEO 🔥", url=item["url"])],
        [
            InlineKeyboardButton("👥 GRUP 1", url="https://t.me/joinchat/j4cRH_jg7VJhN2I1"),
            InlineKeyboardButton("👥 GRUP 2", url="https://t.me/joinchat/JdpYxovFx3IyMjg1")
        ],
        [InlineKeyboardButton("⭐ Join Channel ⭐", url="https://t.me/BokepSenjaBot")],
        [InlineKeyboardButton("🔄 Cari Video Lainnya 🔄", url="https://t.me/Bokep2025Bot?start=next")]
    ]
    return InlineKeyboardMarkup(keyboard)

# === Kirim foto + video ===
async def send_photo_and_video(chat_id, item, client):
    reply_markup = build_keyboard(item)
    caption = f"**📺 {item['title']}**\n\n©️__Bokepsenja.com__\n\u200b"

    
    
    # lanjut kirim video jika ada
    if item.get("videos"):
        await client.send_video(
            chat_id=chat_id,
            video=item["videos"],
            caption=caption,
            reply_markup=reply_markup
        )

# === Command /start ===
@app.on_message(filters.command("start"))
async def start_command(client, message):
    
    # kirim pesan loading dulu
    searching_msg = await message.reply("⏳ Mencari video ...")

    item = await get_random_item()
    if not item:
        await searching_msg.edit("⚠️ Data tidak ditemukan dari API.")
        return

    # kirim video
    await send_photo_and_video(message.chat.id, item, client)

    # hapus pesan "Mencari video ..."
    await searching_msg.delete()

# === Callback Handler ===
@app.on_callback_query()
async def callback_handler(client, callback_query):
    if callback_query.data == "next":
        item = await get_random_item()
        if not item:
            await callback_query.answer("⚠️ Tidak ada data dari API.", show_alert=True)
            return

        # hapus pesan lama biar gak error MESSAGE_NOT_MODIFIED
        try:
            await callback_query.message.delete()
        except:
            pass

        await send_photo_and_video(callback_query.message.chat.id, item, client)
        await callback_query.answer()

# === Event: User Baru Masuk Grup ===
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

# === Run bot ===
if __name__ == "__main__":
    print("✅ Bot sudah jalan dan terkoneksi ke API PHP")
    app.run()
