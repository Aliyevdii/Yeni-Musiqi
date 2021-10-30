from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import Client, filters
from helpers.decorators import sudo_users_only
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery


@Client.on_message(command(["yenile", "reboot"]) & ~filters.edited)
@sudo_users_only
@check_heroku
async def gib_yenile(client, message, hap):
    msg_ = await message.reply_photo(
                                     photo="https://te.legra.ph/file/813885c3687f7a6277315.jpg", 
                                     caption="**Yenileniyor**\n**Lütfen bekleyin**\n**Muhtemelen 5 dakika sürecektir...**",
   reply_markup=InlineKeyboardMarkup(
        [
             [
                  InlineKeyboardButton(
                      "⚙ Geliştirici" , url ="https://t.me/Bir_Beyfendi")
             ]
        ]
    )
)
    hap.restart()
