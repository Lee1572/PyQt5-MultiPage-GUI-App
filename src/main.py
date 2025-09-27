import sys
import os
from PyQt5 import QtWidgets
from login_window import LoginWindow

def main():
    """Main function to start the PyQt5 application."""
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()