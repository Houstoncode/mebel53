import sys

import sqlalchemy
from sqlalchemy import create_engine
from PyQt5 import QtWidgets
from dotenv import dotenv_values
from ui.MainUi import MainUi

if __name__ == "__main__":
    config = dotenv_values(".env")

    app = QtWidgets.QApplication(sys.argv)

    main_ui = MainUi()
    main_ui.showLogin()

    app.exec()
