from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
#Bir_Beyfendi

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(client: Client, message: Message):
    await message.reply_photo(photo_text="https://i.ibb.co/MpdcXYM/IMG-20211023-135851-221.jpg",
    caption="**Salak {} 🎵\n Mən {}!\n Səsli söhbətlərdə musiqi oxuya bilən botum.\n Qadağaya ehtiyac olmadan (istifadəçilərə qadağa) səsli çatları idarə etmək, mesajları silmək və Link ilə dəvət etmək icazəsi verməklə Assistenti qrupa əlavə edin.\n Komandalar üçün, /bilgi əmri .**").format(
message.from_user.mention, bot
),
    reply_markup=InlineKeyboardMarkub(
            [
                [
                    InlineKeyboardButton(
                        "➕ Məni Grubuna eklə ➕", url="https://t.me/NexusMusiicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Support Grubu", url="https://t.me/NEXUS_MMC"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👨🏻‍💻 Sahibi", url = "https://t.me/A_l_i_y_e_v_d_i"
                    ),
                    InlineKeyboardButton(
                        "👨🏻‍🎤 Asistan" , url = "https://t.me/NexusAsistan"
                    )
                ],
                [ 
                    InlineKeyboardButton(
                        "🌀 Əmirlər" , url = "https://telegra.ph/Komutlar-10-22"
                    ),
                    InlineKeyboardButton(
                        "🎮 Oyun Botu", url="https://t.me/Nexus_soz_game_bot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
   )

@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(f"**Salam {message.from_user.mention}!\n Bu botun məlumat menyusu 🤓\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 /ytp <Sorgu> - youtube üzerinden çalma\n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n Yalnızca yöneticiler için..\n ▶️ /devam - şarkı çalmaya devam et\n ⏹ /bitir - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n 🎚 /ses asistan hesabın ses seviyesini kontrol et\n\n ⚪ /katil - Müzik asistanı grubunuza katılır\n ⚫ /ayril - Müzik asistanı grubunuzu terk eder.\n\n ❗ Not:\n Botun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n - Mesaj silme yetkisi,\n - Bağlantı ile davet etme yetkisi,\n - Sesli sohbeti yönetme yetkisi.**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "👨🏻‍💻 Sahibi", url="https://t.me/A_l_i_y_e_v_d_i")
                 ]
             ]
         )
    )
