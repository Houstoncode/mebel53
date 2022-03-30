from PyQt5 import QtWidgets

from database.models.UserModel import UserModel
from ui.designer.forms.register_window import Ui_Register
from ui.forms.ModalError import open_modal


class RegisterWindow(QtWidgets.QMainWindow, Ui_Register):
    def __init__(self, redirect):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.redirect_to_login.clicked.connect(redirect('login'))
        self.redirectToDashboard = redirect('dashboard')
        self.register_btn.clicked.connect(self.handleRegister)

    def handleRegister(self):
        emailValue = self.email_input.text()
        passwordValue = self.password_input.text()
        fullNameValue = self.fullname_input.text()

        if not emailValue or not passwordValue or not fullNameValue:
            open_modal(self, 'warning', 'Заполните данные',
                       'Пожалуйста, заполните все поля!')
            return

        userModel = UserModel()
        user = userModel.createUser(email=emailValue, password=passwordValue, full_name=fullNameValue)

        if user is None:
            open_modal(self, 'error', 'Попробуйте заново!',
                       'Пользователь с таким e-mail уже зарегистрирован!')
            return

        self.redirectToDashboard()