from PyQt5.QtWidgets import QMessageBox


def open_modal(self, type_, title, message):
    if type_ == 'error':
        QMessageBox.critical(
            self,
            title,
            message
        )
    elif type_ == 'warning':
        QMessageBox.warning(
            self,
            title,
            message
        )

