import os
import re
import random
from asyncio import sleep as lvda
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/26aec6d41ffd788f624d9.jpg",
    "https://telegra.ph/file/26aec6d41ffd788f624d9.jpg",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ ᴅᴇᴠ ✘ ʀᴏʙᴏᴛ​**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝐃𝐄𝐕](https://t.me/devarora0981)** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/Dev_managerbot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/we_rfriends"),
        ]
    ]
    ran = random.choice(PHOTO)
    l = await event.reply("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ...")
    await lvda(1)
    o = await l.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ.........")
    await lvda(1)
    d = await o.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ...")
    await lvda(1)
    a = await d.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ.........")
    await lvda(1)
    await a.delete()
    # x = await tbot.send_file(event.chat_id, file="CAACAgUAAx0CWOSA3AABBtPDYsX2Vt5j5vHwrarbQLgTX1kO-LQAAvAIAAJicH0p17vHbwZpufkpBA")
    # await lvda(1.5)
    # await x.delete()
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


## Alive mod
# By Hyper
