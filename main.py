# Copyright (c) 2022 NotDankEnough (ilotterytea)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from telegram.ext import ApplicationBuilder

from src.utils.Configuration import cfg
from src.utils.Registrator import registerAllCommands

if __name__ == "__main__":
    # Creating a new Telegram app:
    app = ApplicationBuilder().token(cfg.get("IDENTITY", "TELEGRAM_TOKEN")).build()

    # Handle commands for Telegram app:
    registerAllCommands(app)

    # Polling updates from Telegram:
    app.run_polling()
