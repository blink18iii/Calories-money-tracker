import datetime as dt

date_format = '%d.%m.%Y'


class Record:
    """Создаёт записи."""

    def __init__(self, amount: float, comment: str, date=None):
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, date_format).date()
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
        return sum([record.amount
                    for record in self.records
                    if record.date == dt.date.today()])

    def get_week_stats(self) -> float:
        """Сколько потрачено за 7 дней без сегодня."""
        date_week_ago = dt.date.today() - dt.timedelta(days=7)
        return float(sum([record.amount
                          for record in self.records
                          if date_week_ago < record.date <= dt.date.today()]))

    def get_today_remained(self) -> float:
        """Сколько еще можно потратить за сегодня."""
        spent_today = self.get_today_stats()
        return self.limit - spent_today


class CashCalculator(Calculator):
    USD_RATE = float(70.0)
    EURO_RATE = float(80.0)

    def get_today_cash_remained(self, currency):
        today_stats = self.get_today_stats()
        other_limit = self.limit - today_stats
        currencies = {
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro'),
            'rub': (1, 'руб')
        }

        if currency in currencies:
            currency_rate = currencies[currency][0]
            currency_name = currencies[currency][1]
        else:
            return ('Валюта не найдена')
        if today_stats < self.limit:
            return ('На сегодня осталось '
                    f'{round(other_limit / currency_rate, 2)} '
                    f'{currency_name}')
        elif today_stats == self.limit:
            return ('Денег нет, держись')
        elif today_stats > self.limit:
            debt = abs(other_limit)
            return ('Денег нет, держись: твой долг - '
                    f'{round(debt / currency_rate, 2)} {currency_name}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> str:
        """Сколько можно еще съесть за сегодня."""
        spent_today = round(self.get_today_remained())
        if spent_today > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {spent_today} кКал')
        else:
            return 'Хватит есть!'
