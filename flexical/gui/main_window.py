import random

from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMainWindow, QLabel, QHBoxLayout

from flexical.data.calendar import FlxCalendar
from flexical.gui.calendar_panel import CalendarPanel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.cal = FlxCalendar()

        vbox = QVBoxLayout()

        widget_year = QWidget()

        hbox_year = QHBoxLayout()

        self.prev_year = QPushButton(f"<< {str(self.cal.get_prev_month_year())} <<")
        hbox_year.addWidget(self.prev_year)

        self.cur_year = QLabel(str(self.cal.get_month_year()))
        hbox_year.addWidget(self.cur_year)

        self.next_year = QPushButton(f">> {str(self.cal.get_next_month_year())} >>")
        hbox_year.addWidget(self.next_year)

        self.prev_year.clicked.connect(self.move_to_prev_month)
        self.next_year.clicked.connect(self.move_to_next_month)

        widget_year.setLayout(hbox_year)
        vbox.addWidget(widget_year)

        self.calendar_panel = CalendarPanel()
        self.calendar_panel.first_day = self.cal.get_starting_weekday_of_month()
        self.calendar_panel.prev_month_tail = self.cal.get_prev_month_tail(self.calendar_panel.first_day)
        self.calendar_panel.cur_month = self.cal.get_cur_month_days()
        self.calendar_panel.show_month_grid()
        vbox.addWidget(self.calendar_panel)

        self.setLayout(vbox)

    @QtCore.Slot()
    def move_to_prev_month(self):
        self.cal.shift_month_back()
        self.update_month()

    @QtCore.Slot()
    def move_to_next_month(self):
        self.cal.shift_month_forth()
        self.update_month()

    def update_month(self):
        self.prev_year.setText(self.cal.get_prev_month_year())
        self.cur_year.setText(self.cal.get_month_year())
        self.next_year.setText(self.cal.get_next_month_year())
        self.calendar_panel.first_day = self.cal.get_starting_weekday_of_month()
        self.calendar_panel.prev_month_tail = self.cal.get_prev_month_tail(self.calendar_panel.first_day)
        self.calendar_panel.cur_month = self.cal.get_cur_month_days()
