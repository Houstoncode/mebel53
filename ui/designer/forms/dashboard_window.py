# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.hello_msg = QtWidgets.QLabel(self.centralwidget)
        self.hello_msg.setGeometry(QtCore.QRect(70, 10, 651, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.hello_msg.setFont(font)
        self.hello_msg.setObjectName("hello_msg")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(80, 211, 601, 291))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 180, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        Dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dashboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        Dashboard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dashboard)
        self.statusbar.setObjectName("statusbar")
        Dashboard.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(Dashboard)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(Dashboard)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action_2)
        self.menu_3.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Главный кабинет"))
        self.hello_msg.setText(_translate("Dashboard", "ДОБРО ПОЖАЛОВАТЬ!"))
        self.label_2.setText(_translate("Dashboard", "ПОСЛЕДНИЕ ПРОДАЖИ"))
        self.menu.setTitle(_translate("Dashboard", "Главная"))
        self.menu_2.setTitle(_translate("Dashboard", "Мебель"))
        self.menu_3.setTitle(_translate("Dashboard", "Клиенты"))
        self.action.setText(_translate("Dashboard", "Продажи"))
        self.action_2.setText(_translate("Dashboard", "Выход"))

