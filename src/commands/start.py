# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from telegram import Update
from telegram.ext import ContextTypes

async def Start(upd: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await upd.message.reply_text("""👋 Hello, {name}!
ℹ️ I'm a media uploader bot and I can upload media that you sent.

<b>🏃 How to start?</b>
Just send a media <i>(photo, video, file, etc.)</i> and I'll upload on your preferred media 
storage service. After uploading, I return an URL link of media and you can share with someone in chat 
messengers that don't support images, like Twitch chats. 

📂 Default media storage service: <b><a href=\"https://i.ilotterytea.kz/\">Picturebin (Maintained by ilotterytea)</a></b>

🌐 You can set custom host for uploading images, like imgur.com or s-ul.eu. Send /service for more info!
""".format(name=upd.message.from_user.first_name), parse_mode='HTML', reply_to_message_id=upd.message.message_id)
