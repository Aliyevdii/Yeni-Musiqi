from asyncio.queues import QueueEmpty
 
from pyrogram import Client, filters 
from pyrogram.types import Message
from helpers.channelmusic import get_chat_id
from cache.admins import admins

import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("durdur") & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'Duraklatıldı'
    ):
        await message.reply_text("❗ Hiçbir şey çalmıyor!")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("▶️ **Müzik duraklatıldı!**\n\n• Müzik kullanımına devam etmek için **komut » devam**") 


@Client.on_message(command("devam") & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'Oynanıyor'
    ):
        await message.reply_text("❗ Hiçbir şey duraklatılmadı!")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("⏸ **Müzik devam ediyor!**\n\n• Kullanımı duraklatmak için **komut » durdur**")


@Client.on_message(command("bitir") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Hiçbir şey yayınlanmıyor!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("✅ **Müzik durduruldu!**\n\n• **Userbot'un sesli sohbet bağlantısı kesildi**")


@Client.on_message(command("atla") & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Atlatılacak müzik yok!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )

        await message.reply_text("⏭️ **__Şarkı bir sonraki kuyruğa atlatıldı__**")

@Client.on_message(command("ver"))
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("Kullanıcıya Yetki Vermek için yanıtlayınız!")
        return
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanıcı yetkili.")
    else:
        await message.reply("✔ Kullanıcı Zaten Yetkili!")


@Client.on_message(command("al"))
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("✘ Kullanıcıyı yetkisizleştirmek için mesajı yanıtlayınız!")
        return
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanıcı yetkisiz")
    else:
        await message.reply("✔ Kullanıcının yetkisi alındı!")


@Client.on_message(command(["ses"]) & other_filters)
@authorized_users_only
async def ses(client, message):
    range = message.command[1]
    chat_id = message.chat.id
    try:
       callsmusic.pytgcalls.change_volume_call(chat_id, volume=int(range))
       await message.reply(f"✅ **Birim olarak ayarlandı:** ```{range}%```")
    except Exception as e:
       await message.reply(f"**hata:** {e}")

@Client.on_message(command("help") & filters.group & ~ filters.edited)
async def helper(client , message:Message):
await message.reply_text(f"""**Selam {message.from_user.mention}!\n Bu botun yardım menüsü 🤩\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 /ytp <Sorgu> - youtube üzerinden çalma\n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n Yalnızca yöneticiler için..\n ▶️ /devam - şarkı çalmaya devam et\n ⏹ /bitir - müzik çalmayı durdurma\n 🔼 /ver botun komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun komutlarını kullanabilen kullanıcının yetkisini al\n 🎚 /ses asistan hesabın ses seviyesini kontrol et\n\n ⚪ /katil - Müzik asistanı grubunuza katılır\n ⚫ /ayril - Müzik asistanı grubunuzu terk eder.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙ Geliştirici", url="https://t.me/Bir_Beyfendi")
                ]
            ]
        )
   )
