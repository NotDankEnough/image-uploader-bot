# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import logging
from datetime import datetime

from os.path import exists
from os import mkdir

# Create /logs/ folder if not exists:
if not exists("logs"):
    mkdir("logs")

# Setting the configuration for logger:
logging.basicConfig(
    filename="logs/{:%Y-%m-%d}.log".format(datetime.now()),

    filemode='w',
    level=logging.DEBUG,
    format="[%(levelname)s] %(asctime)s - %(name)s: %(message)s"
)
