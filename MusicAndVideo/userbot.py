import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("â¡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>ð ð¿ð¾ð½ð¶</b> `{delta_ping * 1000:.3f} ms` \n<b>â³ ð°ð²ðð¸ðð´</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**â á´sá´ÊÊá´á´ Êá´sá´á´Êá´á´á´**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>â¤ï¸ Êá´ÊÊá´ {m.from_user.mention}!

ð   Há´Êá´ Má´É´á´

Â» á´á´á´á´á´É´á´s Òá´Ê á´á´ á´ÊÊá´É´á´

â¢ {HNDLR}á´Êá´Ê [sá´É´É¢ á´Éªá´á´Ê|Êá´á´á´á´Êá´ ÊÉªÉ´á´| Êá´á´ÊÊ á´á´á´Éªá´-ÒÉªÊá´] - Tá´ á´Êá´Ê á´Êá´ sá´É´É¢
â¢ {HNDLR}á´ á´Êá´Ê [á´ Éªá´á´á´ á´Éªá´Êá´| Êá´á´á´á´Êá´ ÊÉªÉ´á´ | Êá´á´ÊÊ á´ Éªá´á´á´ ÒÉªÊá´] - á´á´ á´Êá´Ê á´ Éªá´á´á´ 
â¢ {HNDLR}á´Êá´ÊÊÉªsá´ á´á´ á´ Éªá´á´¡ á´ Éªá´á´á´ 
â¢ {HNDLR}á´ÉªÉ´É¢ - á´á´ á´Êá´á´á´ sá´á´á´á´s
â¢ {HNDLR}Êá´Êá´ - á´á´ á´ Éªá´á´¡ á´ ÊÉªsá´ á´Ò á´á´á´á´á´É´á´

Â»á´á´á´á´á´É´á´s á´á´Ê á´ÊÊ á´á´á´ÉªÉ´s

â¢ {HNDLR}Êá´sá´á´á´ - á´á´ á´á´É´á´ÉªÉ´á´á´ á´Êá´ÊÉªÉ´É¢ á´Êá´ sá´É´É¢ á´Ê á´ Éªá´á´á´ 
â¢ {HNDLR}á´á´á´sá´ - á´á´ á´á´á´sá´ á´Êá´ á´Êá´ÊÊá´á´á´ á´Ò á´ sá´É´É¢ á´Ê á´ Éªá´á´á´ 
â¢ {HNDLR}sá´Éªá´ - á´á´ sá´Éªá´ á´ sá´É´É¢ á´Ê á´ Éªá´á´á´ 
â¢ {HNDLR}á´É´á´ - á´á´ á´É´á´ á´Êá´ÊÊá´á´á´ </b>
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo", "sumit", "openbaby"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>â¤ï¸ Êá´ÊÊá´ {m.from_user.mention}!
      âª á´ÊÉ´á´ á´á´ê±Éªá´ âª

 á´á´Êá´É¢Êá´á´ Usá´ÊÊá´á´ á´á´ á´Êá´Ê sá´É´É¢s á´É´á´ á´ Éªá´á´á´s ÉªÉ´ á´á´Êá´É¢Êá´á´ á´ á´Éªá´á´ á´Êá´á´ á´á´á´ á´Êá´á´á´á´ ÊÊ ê±á´á´Êá´á´Ê á´Êá´Êá´Êá´.

Â»  sá´Êsá´ÊÉªÊá´ á´á´Ê á´Êá´É´É´á´Ê:-
â¢ [á´á´á´á´á´á´](https://t.me/cute_friendx)


Â»  âª á´á´ÉªÉ´ sá´á´á´á´Êá´ É¢Êá´á´á´ âª
 â¢ ÒÉªÊsá´ á´á´ÉªÉ´ sá´á´á´á´Êá´ É¢Êá´á´á´ á´É´á´ á´Êá´É´ á´Êá´á´ #Dyna-Music-Userbot
Â» sá´á´á´á´Êá´ É¢Êá´á´á´ || [sá´á´á´á´Êá´](https://t.me/cute_friendx) 
 
 </b>
"""
    await m.reply(REPO, disable_web_page_preview=True)
