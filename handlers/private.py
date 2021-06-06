from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Merhaba, Ben {bn} 🎵
Göründügü gibi müzik uygulaması yapıyoruz sizler için en iyisini tasarladık. Ben [Mehmet Bey](https://t.me/EfsaneStar).
Ve bu uygulamada emeği geçen arkadaşım [RGMehmet](https://t.me/mehmett_12) Kendisine teşekkürler ederim.👍
Bu uygulamayı grubunuza ekleyin ve özgürce müzik çalın!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Katkıda bulunan 👨‍💻", url="https://t.me/Mehmett_12")
                  ],[
                    InlineKeyboardButton(
                        " Sohbet Group 💬", url="https://t.me/sohbetskyfall"
                    ),
                    InlineKeyboardButton(
                        " Uygulama sahibi 👨‍💻", url="https://t.me/EfsaneStar"
                    )
                ],[ 
                    InlineKeyboardButton(
                        " Support group 🎛️", url="https://t.me/RgBotSupport"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/sohbetlobisi")
                ]
            ]
        )
   )
