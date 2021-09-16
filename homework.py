import datetime as dt

date_format = '%d.%m.%Y'


class Calculator:
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records = []




class Record:
    def __init__(self, amount: float, date: str, comment: str = None):
        self.amount = float(amount)
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, date_format)
        else:
            self.date = dt.datetime.today()
