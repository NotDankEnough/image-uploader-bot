# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from telegram import Update
from telegram.ext import ContextTypes

from re import split
from requests import post

from src.utils.Configuration import cfg

async def Media(upd: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    url = split(r"(?<!\\)\+", cfg.get("DEFAULT", "MEDIA_STORAGE_SERVICE"))

    tgFile = await upd.message.photo[0].get_file()
    array = await tgFile.download_as_bytearray()

    request = post(
        url=url[0],
        files={
            url[1]: array
        }
    )

    await upd.message.reply_text(request.text)
