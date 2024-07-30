from src.processing import filter_by_currencies, filter_by_state, sort_by_date
from src.sorting import get_transactions_sort_search
from src.utils import get_data_transactions
from src.widget import get_data, mask_account_card

print(
    "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
    "Выберите необходимый пункт меню:\n"
    "1. Получить информацию о транзакциях из JSON-файла\n"
    "2. Получить информацию о транзакциях из CSV-файла\n"
    "3. Получить информацию о транзакциях из XLSX-файла\n"
)
item = input()
transactions = []

while item != "1" and item != "2" and item != "3":
    item = input("Введите корректный пункт меню: ")

if item == "1":
    print("Для обработки выбран JSON-файл")
    transactions = get_data_transactions("data/operations.json")
elif item == "2":
    print("Для обработки выбран CSV-файл")
    transactions = get_data_transactions("data/transactions.csv")
elif item == "3":
    print("Для обработки выбран XLSX-файл")
    transactions = get_data_transactions("data/transactions_excel.xlsx")

state_str = (
    "Введите статус, по которому необходимо выполнить фильтрацию.\n"
    "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
)

state = input(state_str).upper()

while state.upper() != "EXECUTED" and state.upper() != "CANCELED" and state.upper() != "PENDING":
    print(f"Статус операции '{state}' недоступен.")
    state = input(state_str).upper()

if state == "EXECUTED":
    print("Операции отфильтрованы по статусу 'EXECUTED'")
    transactions = filter_by_state(transactions)
elif state == "CANCELED":
    print("Операции отфильтрованы по статусу 'CANCELED'")
    transactions = filter_by_state(transactions, state)
elif state == "PENDING":
    print("Операции отфильтрованы по статусу 'PENDING'")
    transactions = filter_by_state(transactions, state)

sort_date = input("Отсортировать операции по дате? ДА/НЕТ\n")

while sort_date.upper() != "ДА" and sort_date.upper() != "НЕТ":
    sort_date = input("Отсортировать операции по дате? ДА/НЕТ\n")

if sort_date.upper() == "ДА":
    ascending = input("Отсортировать по возрастанию или по убыванию?\n")
    while ascending.lower() != "по возрастанию" and ascending.lower() != "по убыванию":
        ascending = input("Отсортировать по возрастанию или по убыванию?\n")
    if ascending.upper() == "по возрастанию":
        ascending_ = True
        transactions = sort_by_date(transactions, ascending_)
    else:
        ascending_ = False
        transactions = sort_by_date(transactions, ascending_)

rub_transactions = input("Выводить только рублевые тразакции? ДА/НЕТ\n")

while rub_transactions.upper() != "ДА" and rub_transactions.upper() != "НЕТ":
    rub_transactions = input("Выводить только рублевые тразакции? Да/Нет\n")

if rub_transactions.upper() == "ДА":
    transactions = filter_by_currencies(transactions, ["RUB"])

filter_transactions = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")

while filter_transactions.upper() != "ДА" and filter_transactions.upper() != "НЕТ":
    filter_transactions = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")

if filter_transactions.upper() == "ДА":
    search_string = input("Введите строку для поиска: ")
    transactions = get_transactions_sort_search(transactions, search_string)

print("Распечатываю итоговый список:\n")
if not transactions:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
else:
    print(f"Всего банковских операций в выборке: {len(transactions)}")
    for transaction in transactions:
        print(get_data(transaction["date"]), transaction["description"])
        print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
        print(
            f"Сумма: {transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}\n")
