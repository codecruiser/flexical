from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class FlxCalendar:
    dt = None
    year = None
    month = None
    day = None
    fst_day_month = None

    def __init__(self):
        t_now = datetime.now()
        self.set_current_props(t_now)

    def set_current_props(self, dt):
        self.dt = dt
        self.year = dt.year
        self.month = dt.month
        self.day = dt.day
        self.fst_day_month = dt.replace(day=1)

    def get_month_year(self):
        return f"{self.dt.month} {self.dt.year}"

    def get_prev_month_year(self):
        prev_m_dt = self.dt - relativedelta(months=1)
        return f"{prev_m_dt.month} {prev_m_dt.year}"

    def get_next_month_year(self):
        next_m_dt = self.dt + relativedelta(months=1)
        return f"{next_m_dt.month} {next_m_dt.year}"

    def shift_month_back(self):
        self.dt = self.dt - relativedelta(months=1)

    def shift_month_forth(self):
        self.dt = self.dt + relativedelta(months=1)

    def get_starting_weekday_of_month(self):
        return self.dt.replace(day=1).weekday()

    def get_prev_month_tail(self, how_many_days):
        """
        What days from a previous month still fit in the first week of the next

        :param how_many_days:
        :return:
        """
        return [
            self.dt.replace(day=1) - relativedelta(days=i)
            for i in range(how_many_days, 0, -1)
        ]

    def get_cur_month_days(self):
        return [
            self.dt + relativedelta(days=i)
            for i in range(31) if (self.dt + relativedelta(days=i)).month == self.dt.month
        ]

