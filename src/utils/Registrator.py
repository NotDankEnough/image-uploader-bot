# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from telegram.ext import CommandHandler, Application, MessageHandler
from telegram.ext.filters import BaseFilter, AUDIO, VIDEO, PHOTO, ATTACHMENT

from src.commands.start import Start
from src.commands.media import Media
from src.commands.service import Service

def registerAllCommands(application: Application) -> None:
    """
    Register commands for application.
    :param application: Telegram application.
    """

    application.add_handler(CommandHandler("start", Start))
    application.add_handler(CommandHandler("service", Service))
    application.add_handler(MessageHandler(BaseFilter(AUDIO | VIDEO | PHOTO | ATTACHMENT), Media))
