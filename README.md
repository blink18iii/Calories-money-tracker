## Два калькулятора: для подсчёта денег и калорий.
Пользовательской части(интерфейса) калькуляторов нет.

## Как запустить проект:

Клонировать репозиторий:
```
git clone https://github.com/blink18iii/hw_python_oop
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv

. venv/Scripts/activate
```
Не забудьте установить правильный интерпретатор.

Установить зависимости из файла requirements.txt:
```
cd hw_python_oop/

python -m pip install --upgrade pip

pip install -r requirements.txt
```

## Калькулятор денег умеет:
<ol>
<li>Сохранять новую запись о расходах методом add_record()</li>
<li>Считать, сколько денег потрачено сегодня методом get_today_stats()</li>
<li>Калькулятор калорий должен уметь:</li>
<li>Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод get_today_cash_remained(currency)</li>
<li>Считать, сколько денег потрачено за последние 7 дней — метод get_week_stats()</li>
<li>Сохранять новую запись о приёме пищи— метод add_record()</li>
<li>Считать, сколько калорий уже съедено сегодня — метод get_today_stats()</li>
<li>Определять, сколько ещё калорий можно/нужно получить сегодня — метод get_calories_remained()</li>
<li>Считать, сколько калорий получено за последние 7 дней — метод get_week_stats()</li>
<li>У калькуляторов много пересекающихся функций: они должны уметь хранить какие-то записи
(о еде или деньгах, но по сути - всё числа и даты), знать дневной лимит (сколько в день можно истратить денег или сколько калорий можно получить)
и суммировать записи за конкретные даты. Всю эту общую функциональность заложите в родительский класс Calculator, а от него унаследуйте классы CaloriesCalculator и CashCalculator.</li>
</ol>

Конструктор класса Calculator принимает один аргумент — число limit (дневной лимит трат/калорий, который задал пользователь).

Чтобы было удобнее создавать записи, есть отдельный класс Record. В нём вы сохраните:

число amount (денежная сумма или количество килокалорий),
комментарий comment, поясняющий, на что потрачены деньги или откуда взялись калории,
дату создания записи date (передаётся в явном виде в конструктор, либо присваивается значение по умолчанию — текущая дата).
Примеры таких записей:

```
cash_calc = CashCalculator(1000) # Ставим лимит на деньги
calories_calc = CaloriesCalculator(1000) # Ставим лимит на калории
cash_calc.add_record(Record(amount=800, comment='pizza')) # Создаем запись потраченных денег
print(cash_calc.get_today_cash_remained('rub')) # Проверяем остаток денег после покупки
print(calories_calc.get_calories_remained()) # Проверяем какой лимит калорий
calories_calc.add_record(Record(amount=100, comment='покушать')) # Едим и отнимаем каллории от лимита
print(calories_calc.get_calories_remained()) # Проверяем какой лимит калорий остался
```

## Подробнее о формате вывода
Метод ```get_calories_remained()``` калькулятора калорий возвращает ответ
«Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал», если лимит ```limit``` не достигнут,
или «Хватит есть!», если ```limit``` достигнут или превышен.
Метод ```get_today_cash_remained(currency)``` денежного калькулятора принимает на вход код валюты: одну из строк "rub", "usd" или "eur". Возвращает он сообщение о состоянии дневного баланса в этой валюте, округляя сумму до двух знаков после запятой (до сотых):
«На сегодня осталось N руб/USD/Euro» — в случае, если лимит ```limit``` не достигнут,
или «Денег нет, держись», если ```limit``` достигнут,
или «Денег нет, держись: твой долг - N руб/USD/Euro», если ```limit``` превышен.
Курс валют укажите константами ```USD_RATE``` и ```EURO_RATE```, прямо в теле класса CashCalculator. Какой курс вы укажете — не так важно, выберите любой, похожий на правду. Значения обменного курса можно посмотреть в интернете.
