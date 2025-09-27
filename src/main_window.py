import sys
import os
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from user_info_window import InfoWindow
from calendar_window import CalendarWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Load UI file from ui folder
        ui_path = os.path.join(os.path.dirname(__file__), '..', 'ui', 'main_menu.ui')
        uic.loadUi(ui_path, self)

        # Find widgets
        self.logo_label = self.findChild(QtWidgets.QLabel, "logoLabel")
        self.welcome_label = self.findChild(QtWidgets.QLabel, "welcomeLabel")
        self.info_button = self.findChild(QtWidgets.QPushButton, "infoButton")
        self.calender_button = self.findChild(QtWidgets.QPushButton, "calenderButton")
        self.quit_button = self.findChild(QtWidgets.QPushButton, "quitButton")
        
        # Debug prints
        print("Main Menu - Logo label found:", self.logo_label is not None)
        print("Main Menu - Welcome label found:", self.welcome_label is not None)
        print("Main Menu - Info button found:", self.info_button is not None)
        print("Main Menu - Calender button found:", self.calender_button is not None)
        print("Main Menu - Quit button found:", self.quit_button is not None)

        # Set the logo image from assets folder
        if self.logo_label:
            logo_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'logo.png')
            if os.path.exists(logo_path):
                pixmap = QtGui.QPixmap(logo_path)
                self.logo_label.setPixmap(pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio))
            else:
                print(f"Logo file not found at: {logo_path}")
        else:
            print("Logo label not found!")
        
        # Set a personalized welcome message
        if self.welcome_label:
            self.welcome_label.setText("Welcome, Lebohang Ramatlapeng!")
        else:
            print("Welcome label not found!")

        # Connect buttons to functions
        if self.info_button:
            self.info_button.clicked.connect(self.open_info_window)
        else:
            print("Info button not found!")
            
        if self.calender_button:
            self.calender_button.clicked.connect(self.open_calendar_window)
        else:
            print("Calender button not found!")
            
        if self.quit_button:
            self.quit_button.clicked.connect(self.close_application)
        else:
            print("Quit button not found!")

    def open_info_window(self):
        """Opens the user information window."""
        self.info_window = InfoWindow()
        self.info_window.show()

    def open_calendar_window(self):
        """Opens the calendar window."""
        self.cal_window = CalendarWindow() 
        self.cal_window.show()

    def close_application(self):
        """Closes the entire application."""
        QtWidgets.QApplication.quit()

if __name__ == "__main__":
    # For testing this window independently
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())