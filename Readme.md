# Project 9

Набор утилит для обработки и маскировки данных финансовых транзакций.

## Структура проекта

* `processing.py` — фильтрация и сортировка транзакций по дате и статусу.
* `masks.py` — маскирование номеров карт и счетов для отображения.
* `widget.py` — набор функций виджета.
* `decorators.py` — декораторы для логирования выполнения функций.

## Возможности

* **Фильтрация транзакций**
  Функция `filter_by_state` возвращает транзакции с заданным статусом (по умолчанию — `EXECUTED`).

* **Сортировка транзакций**
  Функция `sort_by_date` сортирует список транзакций по полю `date` (по убыванию по умолчанию).

* **Маскирование номера карты**
  `get_mask_card_number` скрывает средние цифры номера карты, оставляя первые 6 и последние 4.

* **Маскирование счета**
  `get_mask_account` отображает только последние 4 цифры номера счета.

* **Генерация номеров карт**
  Функция `card_number_generator` генерирует последовательность номеров карт с ведущими нулями и форматированием по группам (4 символа).

* **Разделение строк на группы**
  `split_groups` разбивает строку на группы заданного размера.

* **Получение описаний транзакций**
  `transaction_descriptions` возвращает список всех описаний транзакций.

* **Фильтрация по валюте**
  `filter_by_currency` возвращает транзакции с указанным кодом валюты.

* **Логирование выполнения функций**
  Декоратор `log` фиксирует время начала и окончания работы функции, а также записывает успешный результат или ошибку в консоль или файл.

## Установка

```bash
git clone git@github.com:dagniden/project9.git
poetry install
```

## Пример использования

```python
from processing import filter_by_state, sort_by_date
from masks import get_mask_card_number, get_mask_account
from generators import card_number_generator, transaction_descriptions, filter_by_currency
from decorators import log

@log("log.txt")
def example_func(x, y):
    return x + y

transactions = [
    {"id": 1, "state": "EXECUTED", "date": "2022-01-01T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2022-01-02T10:00:00"},
]

executed = filter_by_state(transactions)
sorted_tx = sort_by_date(executed)

masked_card = get_mask_card_number(1234567812345678)
masked_account = get_mask_account(40817810400001234567)

# Генерация номеров карт
for card in card_number_generator(1, 3):
    print(card)
# Вывод:
# 0000 0000 0000 0001
# 0000 0000 0000 0002

# Получение описаний транзакций
descriptions = transaction_descriptions(transactions)
# ["Оплата услуг", "Перевод на счёт"]

# Фильтрация по валюте
usd_transactions = list(filter_by_currency(transactions, "USD"))
# [{"id": 1, "state": "EXECUTED", ...}]

# Вызов функции с логированием
example_func(1, 2)
# Лог будет сохранён в data/log.txt 
```

## Тестирование

Проект покрыт модульными тестами, расположенными в следующих модулях:

* `test_processing.py` — тесты фильтрации и сортировки транзакций;
* `test_masks.py` — тесты маскирования карт и счетов;
* `test_widget.py` — тесты форматирования даты и маскировки строк;
* `test_generators.py` — тесты генераторов номеров карт и фильтрации по валюте;
* `test_decorators.py` — тесты логирования выполнения функций;
* `conftest.py` — фикстуры и генерация тестовых данных.

Покрытие кода тестами составляет **100%**.
Для генерации отчёта покрытия используется `pytest` с опцией `--cov`.
HTML-отчёт формируется в `htmlcov/index.html` командой:

```
pytest --cov=src --cov-report=html
```
