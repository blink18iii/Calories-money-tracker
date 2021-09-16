import datetime as dt

date_format = '%d.%m.%Y'


class Calculator:
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records = []

    def add_record(self,new_record: str) -> None:
        """Adding new record"""
        self.records.append(new_record)

    def get_today_stats():
        """How much calories were eaten"""
        today_stats = dt.date.today()
        sum(record.amount)

    def get_calories_remained():


    def get_week_stats():
        """Record total week calories"""
        today_stats = dt.date.today()
        week_ago_stats = today_stats - dt.timedelta(days = 7)
        return float(sum(record.amount))


class CashCalculator(Calculator):
    USD_RATE = 80.0
    EURO_RATE = 90.0
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency: float):



class Record:
    """Creating a record"""
    def __init__(self, amount: float, comment: str, date: str = None):
        self.amount = float(amount)
        self.comment = comment
        self.date = date
        if date is not None:
            self.date = dt.datetime.strptime(date, date_format).date()
        else:
            self.date = dt.datetime.today()

