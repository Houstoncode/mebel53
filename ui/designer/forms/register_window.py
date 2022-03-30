# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(800, 528)
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 190, 431, 154))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.fullname_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.fullname_input.setObjectName("fullname_input")
        self.verticalLayout_4.addWidget(self.fullname_input)
        self.email_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.email_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.email_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.email_label.setObjectName("email_label")
        self.verticalLayout_4.addWidget(self.email_label)
        self.email_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.email_input.setObjectName("email_input")
        self.verticalLayout_4.addWidget(self.email_input)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.password_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password_input.setObjectName("password_input")
        self.verticalLayout_2.addWidget(self.password_input)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 89, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.redirect_to_login = QtWidgets.QPushButton(self.centralwidget)
        self.redirect_to_login.setGeometry(QtCore.QRect(410, 390, 191, 32))
        self.redirect_to_login.setObjectName("redirect_to_login")
        self.register_btn = QtWidgets.QPushButton(self.centralwidget)
        self.register_btn.setGeometry(QtCore.QRect(180, 370, 231, 61))
        self.register_btn.setObjectName("register_btn")
        Register.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Register)
        self.statusbar.setObjectName("statusbar")
        Register.setStatusBar(self.statusbar)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "MainWindow"))
        self.label_6.setText(_translate("Register", "ФИО"))
        self.email_label.setText(_translate("Register", "E-MAIL"))
        self.label_5.setText(_translate("Register", "ПАРОЛЬ"))
        self.label.setText(_translate("Register", "РЕГИСТРАЦИЯ"))
        self.redirect_to_login.setText(_translate("Register", "Уже зарегистрированы?"))
        self.register_btn.setText(_translate("Register", "Зарегистрироваться"))

