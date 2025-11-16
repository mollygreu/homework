# Bank Operations Widget

Проект для работы с банковскими операциями — маскирование номеров карт и счетов, а также фильтрация и сортировка данных.

## Установка

```bash
poetry install


## Использование
## Маскирование реквизитов
from src.masks import get_mask_card_number, get_mask_account

print(get_mask_card_number(7000792289606361))
# "7000 79** **** 6361"

print(get_mask_account(73654108430135874305))
# "**4305"

## Обработка операций

from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2024-03-01T10:00:00.000000"},
    {"id": 2, "state": "CANCELED", "date": "2024-02-01T10:00:00.000000"},
]

print(filter_by_state(operations))
print(sort_by_date(operations))
```

### Модуль generators

Добавлены генераторы для обработки транзакций.

Пример использования:
```python
from src.generators import filter_by_currency

usd_ops = filter_by_currency(transactions, "USD")
print(next(usd_ops))

```
## Модуль decorators

В проект добавлен модуль `decorators`, содержащий декоратор `log`.

### log

Декоратор логирует работу функций:

- если передан параметр `filename`, запись идёт в файл;
- если параметр не передан — лог выводится в консоль.

### Пример использования

```python
from decorators.log import log

@log()
def add(a, b):
    return a + b

@log(filename="mylog.txt")
def divide(a, b):
    return a / b
```
Успешный вызов - вывод: 
add ok

Ошибка - вывод: divide error: 
ZeroDivisionError. Inputs: (10, 0), {}
---

