# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from configparser import ConfigParser
import os

from src.utils.Logger import logging


def getConfig(file_path: str) -> ConfigParser:
    """
    Get configuration file. If file path not exists, so just create a new config with params.
    :param file_path: File path to .ini config file.
    :return: ConfigParser
    """

    # Configuration Parser:
    cfg = ConfigParser()

    # If config file exists, so just read it:
    if os.path.exists(file_path):
        logging.info("Configuration file exists in %s", file_path)
        cfg.read(file_path)
    else:
        # Section: IDENTITY:
        cfg.add_section("IDENTITY")
        cfg.set("IDENTITY", "TELEGRAM_TOKEN", "YO_PLACE_YOUR_TELEGRAM_TOKEN_HERE")

        # Section: DEFAULT:
        cfg.add_section("DEFAULT")
        cfg.set("DEFAULT", "MEDIA_STORAGE_SERVICE", "https://i.ilotterytea.kz/upload+file+None+None+None")

        # Writing the configuration file:
        with open(file_path, "w") as file:
            cfg.write(file)
            file.close()

        logging.error(
            "\x1b[31;20m The configuration file was just created in %s! You need to fill in the fields in this file, otherwise the program may not work correctly.\x1b[0m",
            file_path)
        exit(1)

    logging.info("Returning the configuration with %s sections", len(cfg.sections()))
    return cfg


cfg = getConfig("config.ini")
