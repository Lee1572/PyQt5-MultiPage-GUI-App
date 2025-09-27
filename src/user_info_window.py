import sys
import os
from PyQt5 import QtWidgets, uic, QtCore

class InfoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(InfoWindow, self).__init__()
        # Load UI file from ui folder
        ui_path = os.path.join(os.path.dirname(__file__), '..', 'ui', 'user_info.ui')
        uic.loadUi(ui_path, self)

        # Find widgets
        self.name_label = self.findChild(QtWidgets.QLabel, "nameLabel")
        self.student_id_label = self.findChild(QtWidgets.QLabel, "studentIDLabel")
        self.time_label = self.findChild(QtWidgets.QLabel, "timeLabel")
        self.close_button = self.findChild(QtWidgets.QPushButton, "closeButton")
        
        # Debug prints
        print("User Info - Name label found:", self.name_label is not None)
        print("User Info - Student ID label found:", self.student_id_label is not None)
        print("User Info - Time label found:", self.time_label is not None)
        print("User Info - Close button found:", self.close_button is not None)

        # Set personal information
        if self.name_label:
            self.name_label.setText("Lebohang Ramatlapeng")
        else:
            print("Name label not found!")
            
        if self.student_id_label:
            self.student_id_label.setText("18855105")
        else:
            print("Student ID label not found!")

        # Set up the live clock
        if self.time_label:
            # Initialize the time immediately
            self.update_time()
            
            # Set up a timer to update the time every second
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)  # Update every second
        else:
            print("Time label not found!")

        # Connect the close button
        if self.close_button:
            self.close_button.clicked.connect(self.close)
        else:
            print("Close button not found!")

    def update_time(self):
        """Updates the label with the current time."""
        current_time = QtCore.QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss AP')
        self.time_label.setText(f"Current Time: {label_time}")

if __name__ == "__main__":
    # For testing this window independently
    app = QtWidgets.QApplication(sys.argv)
    window = InfoWindow()
    window.show()
    sys.exit(app.exec_())