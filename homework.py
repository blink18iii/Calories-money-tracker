import datetime as dt

date_format = '%d.%m.%Y'
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records = []        
class Calculator:
    pass


class Record:
    def __init__(self,amount: float, date: int, comment: str = None):
        self.amount = float(amount)
        self.date = date
        self.comment = comment

    
    pass
