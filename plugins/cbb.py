#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>Owner : <a href='tg://user?id={OWNER_ID}'>AUIRGA</a>\nUpdates : <a href='https://t.me/hacking_freaks'>Hacking Freaks</a>\nBackup : <a href='https://t.me/Supplywalah'>Supplywalah</a>\nInstaGram : <a href='https://www.instagram.com/supplywala_telegram/'>Follow Now</a>\nSupport Chat : <a href='https://t.me/Supplywala2'>Support</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/supplywala_membership')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
