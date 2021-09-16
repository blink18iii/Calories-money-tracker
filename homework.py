import datetime as dt

date_format = '%d.%m.%Y'


class Calculator:
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records = []

    def add_record()
    def get_today_stats()
    def get_calories_remained()
    def get_week_stats()


class CashCalculator:
    def __init__(self,):
    def add_record(self):
    def get_today_stats():
    def get_today_cash_remained(self, currency: float):
    def get_week_stats(self):


class Record:
    def __init__(self, amount: float, date: str, comment: str = None):
        self.amount = float(amount)
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, date_format)
        else:
            self.date = dt.datetime.today()

