"""
===========================================================
2A XML Downloader

Versão...........: 0.2
Empresa..........: 2A Tecnologia

Arquivo..........: main.py
===========================================================
"""

import os
import sys

from PySide6.QtWidgets import QApplication

from src.database.Database import Database
from src.gui.MainWindow import MainWindow
from src.gui.Style import load_style
from src.utils.Logger import Logger


APP_NAME = "2A XML Downloader"
APP_VERSION = "0.2.0"


class Application:

    def __init__(self):

        self.logger = Logger()

        self.logger.info("=========================================")
        self.logger.info(f"{APP_NAME} {APP_VERSION}")
        self.logger.info("Inicializando sistema...")

        self.create_directories()

        self.database = Database()
        self.database.initialize()

        self.logger.info("Banco de dados inicializado.")

    # --------------------------------------------------

    def create_directories(self):

        folders = [

            "assets",

            "database",

            "logs",

            "temp",

            "xml"

        ]

        for folder in folders:

            if not os.path.exists(folder):

                os.makedirs(folder)

                self.logger.info(f"Pasta criada: {folder}")

    # --------------------------------------------------

    def create_application(self):

        app = QApplication(sys.argv)

        app.setApplicationName(APP_NAME)

        app.setApplicationVersion(APP_VERSION)

        app.setStyleSheet(load_style())

        return app

    # --------------------------------------------------

    def run(self):

        self.logger.info("Abrindo interface...")

        app = self.create_application()

        window = MainWindow()

        window.show()

        self.logger.info("Interface carregada.")

        sys.exit(app.exec())


def main():

    application = Application()

    application.run()


if __name__ == "__main__":

    main()