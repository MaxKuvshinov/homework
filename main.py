from src.processing import get_dicts_by_state, sort_by_date
from src.utils import read_transactions, search_description
from src.widget import get_change_date, get_mask_account_card


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""

    file_paths = {"1": "data/operations.json", "2": "data/transactions.csv", "3": "data/transactions_excel.xlsx"}

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        answer_user = input("Пользователь: ").strip()
        if answer_user in file_paths:
            file_path = file_paths[answer_user]
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
    transactions = read_transactions(file_path)

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:"""
        )
        status = input("Пользователь: ").strip().upper()
        if status in available_statuses:
            break
        else:
            print(f'Статус операции "{status}" недоступен. Попробуйте снова.')
    filtered_transactions = get_dicts_by_state(transactions, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    while True:
        print("Отсортировать операции по дате? Да/Нет:")
        sort_input = input("Пользователь: ").strip().lower()
        if sort_input in ["да", "нет"]:
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
    if sort_input == "да":
        while True:
            print("Отсортировать по возрастанию или по убыванию? ")
            choice_input = input("Пользователь: ").strip().lower()
            if choice_input in ["по возрастанию", "по убыванию"]:
                reverse_order = choice_input == "по убыванию"
                filtered_transactions = sort_by_date(filtered_transactions, reverse=reverse_order)
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет: ")
        user_input = input("Пользователь: ").strip().lower()
        if user_input in ["да", "нет"]:
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
    if user_input == "да":
        filtered_transactions = [
            item
            for item in filtered_transactions
            if item.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ")
        word_input = input("Пользователь: ").strip().lower()
        if word_input == "да":
            print("Введите слово для фильтрации по описанию: ")
            search_word = input("Пользователь: ").strip()
            filtered_transactions = search_description(filtered_transactions, search_word)
            break
        elif word_input == "нет":
            break
    if len(filtered_transactions) > 0:
        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for item in filtered_transactions:
            date = get_change_date(item.get("date"))
            from_ = get_mask_account_card(item.get("from"))
            to_ = get_mask_account_card(item.get("to"))
            description = item.get("description")

            operation_amount = item.get("operationAmount", {})
            amount = operation_amount.get("amount")
            currency = operation_amount.get("currency", {})
            currency_code = currency.get("code")

            if from_ is None:
                print(f"{date} {description}\n{to_}\nСумма: {amount} {currency_code}.2\n")
            else:
                print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency_code}.\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
