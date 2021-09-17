
import datetime as dt

date_format = '%d.%m.%Y'


class Calculator:
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records = []

    def add_record(self, new_record: 'Record') -> None:
        """Добавление новой записи к списку."""
        self.records.append(new_record)

    def get_today_stats(self) -> float:
        """Сколько потрачено сегодня."""
        d_today = dt.date.today()
        return sum([record.amount
                    for record in self.records
                    if record.date == d_today])

    def get_week_stats(self) -> float:
        """Сколько потрачено за 7 дней."""
        d_today = dt.date.today()
        date_week_ago = d_today - dt.timedelta(days=7)
        return float(sum([record.amount
                          for record in self.records
                          if date_week_ago < record.date <= d_today]))


class Record:
    def __init__(self, amount: float, comment: str, date: str = None):
        self.amount: float = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime
        pass

class CashCalculator(Calculator):
    def get_today_cash_remaining(self, currency: str):
        pass

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        pass
    
