"""
===========================================================
2A XML Sync Service

Arquivo........: Logger.py
Descrição......: Registro de eventos

===========================================================
"""

import os
from datetime import datetime


class Logger:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        data = datetime.now().strftime("%Y%m%d")

        self.filename = os.path.join(
            "logs",
            f"{data}.log"
        )

    # ----------------------------------------------------

    def write(self, texto):

        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        linha = f"{agora}  {texto}\n"

        with open(
            self.filename,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(linha)

    # ----------------------------------------------------

    def info(self, texto):

        self.write("[INFO] " + texto)

    # ----------------------------------------------------

    def error(self, texto):

        self.write("[ERRO] " + texto)