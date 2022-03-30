from PyQt5 import QtWidgets

from ui.forms.Dashboard import DashboardWindow
from ui.forms.Login import LoginWindow
from ui.forms.Register import RegisterWindow


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = None

    def redirect(self, name):
        def redirectTo():
            if self.window is not None:
                self.window.hide()

            if name == 'dashboard':
                self.showDashboard()

            if name == 'login':
                self.showLogin()

            if name == 'register':
                self.showRegister()

        return redirectTo

    def showDashboard(self):
        self.window = DashboardWindow(self.redirect)
        self.window.show()

    def showLogin(self):
        self.window = LoginWindow(self.redirect)
        self.window.show()

    def showRegister(self):
        self.window = RegisterWindow(self.redirect)
        self.window.show()
