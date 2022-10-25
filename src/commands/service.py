# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from telegram import Update
from telegram.ext import ContextTypes


async def Service(upd: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    print(upd.MESSAGE)
    await upd.message.reply_text("""🌐 You can set custom host for uploading images, like imgur.com or s-ul.eu - just replace the fields and send command <code>/service REQUEST_URL+FORM_FIELD+EXTRA_HEADERS+IMAGE_LINK+DELETION_LINK</code>. Escape + with \\ if needed.

<b>Examples:</b>

<b>For s-ul.eu:</b>
Replace <code>XXXXXXXXX</code> with your API key that can be obtained <a href=\"https://s-ul.eu/account/configurations\">here</a>.
<code>/service https://s-ul.eu/api/v1/upload?wizard=true&key=XXXXXXXXX+file+None+{{url}}+https://s-ul.eu/delete.php?file={{filename}}&key=XXXXXXXXX</code>

<b>For self-hosted services based on Picbin:</b>
Replace <code>XXXXXXXXX</code> with your API key that can be obtained in <i>Me page</i>. For service that maintained by iLotterytea, <a href=\"https://i.ilotterytea.kz/me\">here</a>. <u>Just replace <code>Authorization</code> header to <code>null</code>, if you don't want to authorize.</u>
<code>/service https://i.yourservice.com/upload+file+Authorization: XXXXXXXXX+None+None</code>

<b>More info in <a href=\"https://wiki.chatterino.com/Image%20Uploader/\">this guide</a>!</b>
""".format(name=upd.message.from_user.first_name), parse_mode='HTML', reply_to_message_id=upd.message.message_id)
