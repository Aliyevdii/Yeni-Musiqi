from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Merhaba, Bu bir müzik asistanı hizmetidir.\n\n ❗️ kurallar:\n   - Sohbete izin yok\n   - Bu sohbette spam yapmayın \n\n 🚨 **USERBOT GRUBUNUZA KATILAMAZSA GRUBUNUZDAN YASAKLANMADIĞINA EMİN OLUN VE GRUBUNUZA MANUEL OLARAK EKLEYİN.**\n\n ⚠️ DİKKAT: Burada bir mesaj gönderiyorsanız Yöneticinin iletinizi göreceği anlamına gelir.\n    - Bu kullanıcıyı gizli gruplara eklemeyin.\n   - Özel bilgileri burada paylaşmayınız. 📚 Bilgi için @Bir_Beyfendi\n\n")
  return                        

 
