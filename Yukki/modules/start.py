#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiAFKBot/blob/master/LICENSE >
#
# All rights reserved.

import time

from pyrogram import filters
from pyrogram.types import Message

from Yukki import app, boot, botname
from Yukki.helpers import get_readable_time


@app.on_message(filters.command(["start", "ping"]))
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"https://telegra.ph/file/a82f511eb98f58a685e32.jpg",
        caption=f"""ʜᴇʟʟᴏ✨ **ᴡᴇʟᴄᴏᴍᴇ {message.from_user.mention()} !**\n
 
 **ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴊᴏɪɴ @Techno_Trickop**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛓ Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ Gʀᴏᴜᴘ",
                        url=f"https://t.me/trickyAfkBot?startgroup=true",
                    )
                ],
                [
        
    
                    InlineKeyboardButton("• Oᴡɴᴇʀ", url=f"https://t.me/herox_xd"),
                    InlineKeyboardButton("• Dᴇᴠᴇʟᴏᴘᴇʀ ", url=f"https://t.me/herox_xd"),
                ],
                [
                    InlineKeyboardButton(
                        "• Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/Amtrickyabhii"
                    ),
                    InlineKeyboardButton(
                        "• Uᴘᴅᴀᴛᴇs", url=f"https://t.me/Aboutez"
                    ),
                ],
                
            ]
        ),
    )
    
    
    

    
