from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


GANDU_BSDK = "https://telegra.ph/file/21ba91a40cf7cdac1c881.mp4"


@client.on_message(filters.command(["repo", "source", "gand"]))
async def repo(client, message):
    await message.reply_animation(
        animation=GANDU_BSDK,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ᴅᴇᴠ ✘ ʀᴏʙᴏᴛ-🇮🇳](t.me/dev_managerbot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝐃𝐄𝐕](t.me/devarora0981)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴅᴇᴠ ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ᴘʀɪᴠᴀᴛᴇ 🥺 sᴏ ᴜsᴇ ᴅᴇᴠ ʀᴏʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="t.me/devarora0981"),
                    InlineKeyboardButton(
                        "• sᴜᴘᴘᴏʀᴛ •",
                        url="https://t.me/we_rfriends",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
