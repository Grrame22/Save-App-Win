import sys

import os

from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.login_button = QPushButton('Login', self)
        self.login_button.move(20, 20)
        self.login_button.clicked.connect(self.save_it)

        self.email_button = QPushButton('Email', self)
        self.email_button.move(20, 78)
        self.email_button.clicked.connect(self.save_it)

        self.password_button = QPushButton('Password', self)
        self.password_button.move(20, 138)
        self.password_button.clicked.connect(self.save_it)

        self.source_button = QPushButton('Source', self)
        self.source_button.move(20, 198)
        self.source_button.clicked.connect(self.save_it)

        self.file_name_button = QPushButton('File name', self)
        self.file_name_button.move(20, 258)
        self.file_name_button.clicked.connect(self.save_it)

        self.login_edit = QLineEdit(self)
        self.login_edit.move(130, 22)

        self.email_edit = QLineEdit(self)
        self.email_edit.move(130, 82)

        self.password_edit = QLineEdit(self)
        self.password_edit.move(130, 142)

        self.source_edit = QLineEdit(self)
        self.source_edit.move(130, 202)

        self.file_name_edit = QLineEdit(self)
        self.file_name_edit.move(130, 262)

        self.setGeometry(500, 500, 360, 460)
        self.setWindowTitle('Save App')
        self.show()

    def save_it(self):
        text_login, login = QInputDialog.getText(self, 'Input Login', 'Enter your Login:')

        if login:
            self.login_edit.setText(str(text_login))

        text_email, email = QInputDialog.getText(self, 'Input Email', 'Enter your Email:')

        if email:
            self.email_edit.setText(str(text_email))

        text_password, password = QInputDialog.getText(self, 'Input Password', 'Enter your Password:')

        if password:
            self.password_edit.setText(str(text_password))

        text_source, source = QInputDialog.getText(self, 'Input Source', 'Enter your Source:')

        if source:
            self.source_edit.setText(str(text_source))

        text_file_name, file_name = QInputDialog.getText(self, 'Input File name', 'Enter your File name:')

        if file_name:
            self.file_name_edit.setText(str(text_file_name))

        with open(text_file_name + ".txt", "w") as txt:
            txt.write("############################################" + "\n" + "\n")
            txt.write("This file contains data from: " + text_source + "\n" + "\n")
            txt.write("Login: " + text_login + "\n" + "\n")
            txt.write("Email: " + text_email + "\n" + "\n")
            txt.write("Password: " + text_password + "\n" + "\n")
            txt.write("Source: " + text_source + "\n" + "\n")
            txt.write("Use my app to be more Productive!" + "\n" + "\n")
            txt.write("#####   #   #   #####   #   #   #####   #   #" + "\n")
            txt.write("#   #    ##       #     #   #   #   #   ##  #" + "\n")
            txt.write("#####    #        #     #####   #   #   # # #" + "\n")
            txt.write("#       #         #     #   #   #   #   #  ##" + "\n")
            txt.write("#      #          #     #   #   #####   #   #" + "\n")
            txt.close()

        save_label = QLabel("Saved!", self)
        save_label.move(145, 330)
        save_label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        save_label.adjustSize()
        save_label.show()

        file_name_label = QLabel("Your file path: " + str(os.path.abspath(text_file_name)), self)
        file_name_label.move(10, 400)
        file_name_label.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
