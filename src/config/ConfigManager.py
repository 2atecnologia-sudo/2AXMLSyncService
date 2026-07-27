import os
import configparser


class ConfigManager:

    
    def __init__(self):

        self.folder = "config"

        self.filename = os.path.join(self.folder, "config.ini")

        print("CONFIG:", os.path.abspath(self.filename))

        self.config = configparser.ConfigParser()

        self.create()

    # --------------------------------------------------

    def create(self):

        os.makedirs(self.folder, exist_ok=True)

        if not os.path.exists(self.filename):

            self.config["GERAL"] = {
                "empresa": "",
                "cnpj": ""
            }

            self.config["CERTIFICADO"] = {
                "tipo": "A1",
                "arquivo": "",
                "senha": "",
                "thumbprint": "",
                "nome": "",
                "configurado": "nao"
      }

            self.config["XML"] = {
                "pasta": "",
                "intervalo": "60"
            }

            self.save()

        self.config.read(self.filename, encoding="utf-8")

    # --------------------------------------------------

    def save(self):

        with open(self.filename, "w", encoding="utf-8") as arquivo:

            self.config.write(arquivo)

    # --------------------------------------------------

    def get(self, section, key, default=""):

        try:
            return self.config[section][key]
        except:
            return default

    # --------------------------------------------------

    def set(self, section, key, value):

        if section not in self.config:

            self.config[section] = {}

        self.config[section][key] = str(value)