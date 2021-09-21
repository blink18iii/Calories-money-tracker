import datetime as dt

DATE_FORMAT = '%d.%m.%Y'


class Record:
    """Создаёт записи."""

    def __init__(self, amount: float, comment: str, date=None):
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()
        else:
            self.date = dt.date.today()


class Calculator:
    """Родительский класс."""
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records = []

    def add_record(self, record: Record) -> None:
        """Добавление новой записи к списку."""
        self.records.append(record)

    def get_today_stats(self) -> float:
        """Сколько потрачено за сегодня."""
        today = dt.datetime.today().date()
        return float(sum(i.amount for i in self.records if i.date == today))

    def get_week_stats(self) -> float:
        """Сколько потрачено за 7 дней без сегодня."""
        today = dt.datetime.today().date()
        date_week_ago = dt.date.today() - dt.timedelta(days=7)
        return float(sum(i.amount for i in self.records
                         if date_week_ago < i.date <= today))

    def get_today_remained(self) -> float:
        """Сколько еще можно потратить за сегодня."""
        spent_today = self.get_today_stats()
        return self.limit - spent_today


class CashCalculator(Calculator):
    USD_RATE = 70.0
    EURO_RATE = 80.0

    def get_today_cash_remained(self, currency):
        cash_remained = self.get_today_remained()
        currencies = {
            "rub": ("руб", 1),
            "usd": ("USD", self.USD_RATE),
            "eur": ("Euro", self.EURO_RATE),
        }
        if cash_remained == 0:
            return 'Денег нет, держись'
        if currency not in currencies:
            return 'Нет такой валюты'
        currency, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        remains_abs = abs(cash_remained)
        if cash_remained > 0:
            return (f'На сегодня осталось '
                    f'{cash_remained} {currency}')
        return ('Денег нет, держись: твой долг - '
                f'{remains_abs} {currency}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> str:
        """Сколько можно еще съесть за сегодня."""
        spent_today = round(self.get_today_remained())
        if spent_today > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {spent_today} кКал')
        return 'Хватит есть!'


cash = CashCalculator(3000)
cash.add_record(Record(amount=1000, comment='pizza'))
print(cash.get_today_cash_remained('rub'))
cash.add_record(Record(amount=1000, comment='pizza'))
print(cash.get_today_cash_remained('rub'))
print(cash.get_today_remained())
print(cash.get_today_cash_remained('eur'))
