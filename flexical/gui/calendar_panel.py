from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout


class DayBox(QWidget):

    def __init__(self, day_number):
        super().__init__()
        self.vbox = QVBoxLayout()
        day_label = QLabel(day_number)
        day_label.setStyleSheet("color: #990000; font-size: 36px; font-weight:bold;")
        self.vbox.addWidget(day_label)
        self.setLayout(self.vbox)
        self.setStyleSheet("background-color: #cccccc; border: 1px solid #666666;text-align: center;height: 80px;")


class CalendarPanel(QWidget):

    first_day = None
    prev_month_tail = []
    cur_month = []
    week_days = ['pn', 'wt', 'sr', 'czw', 'pt', 'so', 'nd']

    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        self.boxes = {}

        self.setLayout(self.grid)

    def show_month_grid(self):
        print(self.first_day)
        print(self.cur_month)
        c = 0
        for i in range(5):
            d = 0
            for j in range(7):
                if i == 0 and d < self.first_day:
                    self.boxes[(j, i)] = DayBox(str(self.prev_month_tail[d].day))
                else:
                    self.boxes[(j, i)] = DayBox(str(self.cur_month[d].day))
                    c += 1
                self.grid.addWidget(self.boxes[(j, i)], i, j)
                d += 1

    def show_month(self):

        pass