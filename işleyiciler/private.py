from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Merhaba, Ben {bn} 🎵
Göründügü gibi müzik uygulaması yapıyoruz sizler için en iyisini tasarladım. Ben [01-Meyitzade-01](https://t.me/pumaefe)
Bu uygulamayı grubunuza ekleyin ve özgürce müzik çalın!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Katkıda bulunan 👨‍💻", url="https://t.me/pumaefe")
                  ],[
                    InlineKeyboardButton(
                        " Sohbet Group 💬", url="https://t.me/hirasetsohbet"
                    ),
                    InlineKeyboardButton(
                        " Uygulama sahibi 👨‍💻", url="https://t.me/pumaefe"
                    )
                ],[ 
                    InlineKeyboardButton(
                        " Support group 🎛️", url="https://t.me/hirasetsohbet"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**hiraset music Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/hiraseticraat")
                ]
            ]
        )
   )
