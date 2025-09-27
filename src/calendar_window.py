import sys
import os
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QMessageBox

class CalendarWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CalendarWindow, self).__init__()
        # Load UI file from ui folder
        ui_path = os.path.join(os.path.dirname(__file__), '..', 'ui', 'calendar.ui')
        uic.loadUi(ui_path, self)

        # Find the calendar widget and button
        self.calendar = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        self.select_date_button = self.findChild(QtWidgets.QPushButton, "selectDateButton")
        self.selected_date_label = self.findChild(QtWidgets.QLabel, "selectedDateLabel")

        # Debug prints
        print("Calendar - Calendar widget found:", self.calendar is not None)
        print("Calendar - Select button found:", self.select_date_button is not None)
        print("Calendar - Date label found:", self.selected_date_label is not None)

        # Connect the button and the calendar's signal
        if self.select_date_button and self.calendar:
            self.select_date_button.clicked.connect(self.get_selected_date)
            self.calendar.selectionChanged.connect(self.show_selected_date)
        else:
            print("Calendar widgets not properly initialized!")

    def show_selected_date(self):
        """Updates the label when a new date is selected."""
        if self.calendar and self.selected_date_label:
            date_selected = self.calendar.selectedDate()
            self.selected_date_label.setText(f"Selected: {date_selected.toString(QtCore.Qt.DefaultLocaleLongDate)}")

    def get_selected_date(self):
        """Shows a message box with the selected date."""
        if self.calendar:
            date_selected = self.calendar.selectedDate()
            QMessageBox.information(self, "Date Selected", f"You have selected: {date_selected.toString()}")

if __name__ == "__main__":
    # For testing this window independently
    app = QtWidgets.QApplication(sys.argv)
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec_())