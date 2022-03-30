from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView

from database.models.FurnitureModel import FurnitureModel
from ui.designer.forms.dashboard_window import Ui_Dashboard


class DashboardFurnitureTableModal(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(DashboardFurnitureTableModal, self).__init__()
        self._data = data


class DashboardWindow(QtWidgets.QMainWindow, Ui_Dashboard):
    def __init__(self, redirect):
        super().__init__()
        self.model = None
        self.setupUi(self)
        self.retranslateUi(self)
        self.redirectTo = redirect
        self.action_2.triggered.connect(redirect('login'))
        self.fillTableDate()

    def fillTableDate(self):
        furnitureModel = FurnitureModel()
        furnitureData = furnitureModel.list()
        self.model = QStandardItemModel(len(furnitureData), 4)
        self.model.setHorizontalHeaderLabels(['ID', 'НАЗВАНИЕ', 'МОДЕЛЬ','ЦЕНА'])
        for index, furniture in enumerate(furnitureData):
            for indexCol, value in enumerate(furniture.values().__reversed__()):
                item = QStandardItem()
                item.setText(str(value))
                self.model.setItem(index, indexCol, item)

        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

