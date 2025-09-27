import sys
import os
from PyQt5 import QtWidgets, uic
from main_window import MainWindow

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), '..', 'ui', 'login.ui')
        uic.loadUi(ui_path, self)

        # Find the widgets WITH DEBUGGING
        self.username_input = self.findChild(QtWidgets.QLineEdit, "usernameLineEdit")
        self.password_input = self.findChild(QtWidgets.QLineEdit, "passwordLineEdit")
        self.login_button = self.findChild(QtWidgets.QPushButton, "loginButton")
        self.cancel_button = self.findChild(QtWidgets.QPushButton, "cancelButton")
        
        # ADD THESE PRINT STATEMENTS
        print("Username input found:", self.username_input is not None)
        print("Password input found:", self.password_input is not None)
        print("Login button found:", self.login_button is not None)
        print("Cancel button found:", self.cancel_button is not None)

        # Connect buttons to functions
        if self.login_button:
            self.login_button.clicked.connect(self.login)
        else:
            print("ERROR: Login button not found!")
            
        if self.cancel_button:
            self.cancel_button.clicked.connect(self.close)
        else:
            print("ERROR: Cancel button not found!")
        
        if self.password_input:
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            print("ERROR: Password input not found!")

    def login(self):
        """Checks the login credentials."""
        username = self.username_input.text()
        password = self.password_input.text()

        # Authentication logic
        if username == "Ramatlapeng" and password == "18855105":
            QtWidgets.QMessageBox.information(self, "Success", "Login Successful!")
            self.open_main_window()
            self.hide()  # Hide the login window
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid username or password.")

    def open_main_window(self):
        """Opens the main application window """
        self.main_window = MainWindow()
        self.main_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())