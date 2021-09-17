import datetime as dt

date_format = '%d.%m.%Y'


class Calculator:
    def __init__(self, limit: float):
        self.limit = limit
        self.records = []

    def add_record(self):
        date_today = dt.date.today()
        pass

    def get_today_stats(self):
        pass

    def get_week_stats(self):
        pass


class Record:
    def __init__(self, amount: float, comment: str, date: str = None):
        pass


class CashCalculator(Calculator):
    def get_today_cash_remaining(self, currency: str):
        pass


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        pass
