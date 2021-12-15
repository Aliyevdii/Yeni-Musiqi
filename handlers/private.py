from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
#Bir_Beyfendi

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(client: Client, message: Message):
    await message.reply_photo("https://i.ibb.co/MpdcXYM/IMG-20211023-135851-221.jpg"),
    await message.reply_text(f"**Salam {message.from_user.mention} 🎵\n Mən {bot}!\n Səsli çatlarda musiqi oxuya bilən botum.\n Qadağa (istifadəçilərə qadağa) səlahiyyəti olmadan Link ilə səsli söhbətləri idarə etməyə, mesajları silməyə və dəvət etməyə və qrupa Assistent göndərməyə imkan verir. .**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Məni Grubuna eklə ➕", url="https://t.me/NexusMusiicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💭 Söhbət Grubu", url="https://t.me/iron_Blood_Gurup"
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
                        "🌐 Support", url="https://t.me/NEXUS_MMC"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(f"**Selam {message.from_user.mention}!\n Bu botun məlumat menüsü 🤓\n\n ▶️ /oynat - mahnı oxutmaq üçün youtube url və ya mahnı faylına cavab verin\n ▶️ /oynat <mahnı adı> - istədiyiniz mahnını ifa edin\n 🔴 /ytp <Sorgu> - youtube-da oynayın\n 🎵 /bul <mahnı adı> - istədiyiniz mahnıları tez tapın\n 🎵 /vbul istədiyiniz videoları tez tapın\n 🔍 /ara <query> - youtube-da təfərrüatlı videolar axtarın\n\n Yalnız adminlər üçündür..\n ▶️ /devam - mahnını ifa etməyə davam edin\n ⏹ /bitir - musiqi çalmağı dayandırın\n 🔼 /ver istifadəçiyə icazə verin ki, bot yalnız administrator üçün mövcud olan əmrlərdən istifadə edə bilsin\n 🔽 /al botun admin əmrlərindən istifadə edə bilən istifadəçi al\n 🎚 /ses köməkçi hesabınızın həcminə nəzarət edin\n\n ⚪ /katil - Musiqi köməkçisi qrupunuza qoşulur\n ⚫ /ayril - Musiqi köməkçisi qrupunuzu tərk edir.\n\n ❗ Diqqət:\n Botun aktiv işləməsi üçün aşağıdakı üç imtiyaz tələb olunur:\n - Mesajları silmək səlahiyyəti,\n - Link vasitəsilə dəvət etmək səlahiyyəti,\n - Səsli çatı idarə etmək səlahiyyəti.**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "👨🏻‍💻 Sahibi", url="https://t.me/A_l_i_y_e_v_d_i")
                 ]
             ]
         )
    )
