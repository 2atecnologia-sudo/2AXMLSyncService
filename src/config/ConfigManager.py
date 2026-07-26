"""
===========================================================
2A XML Downloader

ConfigManager.py
===========================================================
"""

import os
import configparser


class ConfigManager:

    def __init__(self):

        self.folder = "config"

        self.filename = os.path.join(self.folder, "config.ini")

        self.config = configparser.ConfigParser()

        self.create()

    # -------------------------------------------------

    def create(self):

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        if not os.path.exists(self.filename):

            self.config["GERAL"] = {

                "empresa": "",

                "cnpj": ""

            }

            self.config["CERTIFICADO"] = {

                "arquivo": "",

                "senha": ""

            }

            self.config["XML"] = {

                "pasta": "",

                "intervalo": "60"

            }

            with open(self.filename, "w", encoding="utf-8") as file:

                self.config.write(file)

        self.load()

    # -------------------------------------------------

    def load(self):

        self.config.read(self.filename, encoding="utf-8")

    # -------------------------------------------------

    def save(self):

        with open(self.filename, "w", encoding="utf-8") as file:

            self.config.write(file)

    # -------------------------------------------------

    def get(self, section, key, default=""):

        try:

            return self.config[section][key]

        except:

            return default

    # -------------------------------------------------

    def set(self, section, key, value):

        self.config[section][key] = str(value)