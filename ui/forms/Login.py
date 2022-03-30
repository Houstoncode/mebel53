from PyQt5 import QtWidgets

from database.models.UserModel import UserModel
from ui.designer.forms.login_window import Ui_Login
from ui.forms.ModalError import open_modal


class LoginWindow(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self, redirectTo):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.redirectToDashboard = redirectTo('dashboard')
        self.auth_btn.clicked.connect(self.handleAuth)
        self.redirect_to_register.clicked.connect(redirectTo('register'))

    def handleAuth(self):
        emailValue = self.email_input.text()
        passwordValue = self.password_input.text()

        if not emailValue or not passwordValue:
            open_modal(self, 'warning', 'Заполните данные',
                       'Пожалуйста, заполните все поля!')
            return

        userModel = UserModel()
        user = userModel.findUserByEmail(emailValue)

        if user is None:
            open_modal(self, 'error', 'Неуспешная авторизация',
                       'Вы ввели неправильный логин или пароль! Попробуйте еще раз!')
            return

        if user.password == passwordValue:
            self.redirectToDashboard()
        else:
            open_modal(self, 'error', 'Неуспешная авторизация',
                       'Вы ввели неправильный логин или пароль! Попробуйте еще раз!')

