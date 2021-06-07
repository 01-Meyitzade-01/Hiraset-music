from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"👋 Merhaba,Ben hiraset federasyonuna ait müzik asistanı hizmetiyim.\n\n ❗️ kurallar:\n   - Sohbete izin yok\n   - İstenmeyen postaya izin verilmez \n\n 🚨 **ASİSTAN GRUBUNUZA KATILAMAZSA GRUP DAVETI BAĞLANTISI VEYA KULLANICI ADI GÖNDER VEYA BOTU GRUBUMUZA ALIN /ayril vs /katil Komutlarına basınız.**\n\n ⚠️ DİKKAT: Burada bir mesaj gönderiyorsanız Yöneticinin iletinizi göreceği anlamına gelir ve sohbete katılın\n    - Bu kullanıcıyı gizli gruplara eklemeyin.\n   - Özel bilgileri burada paylaşmayın YARDIM için @hirasetsohbet ile iletişime geçiniz\n\n")
  return                        
 
 