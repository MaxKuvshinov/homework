from src.masks import mask_account_number, mask_number_card


def get_mask_account_card(card_or_account: str) -> str:
    """Функция, которая принимает номер карты или счета и маскирует"""
    words = card_or_account.split()
    number = words[-1]
    description = " ".join(words[:-1])

    if number.isdigit() and len(number) in [16]:
        masked_number = mask_number_card(number)
    elif number.isdigit() and len(number) >= 4:
        masked_number = mask_account_number(number)
    else:
        return card_or_account

    return f"{description} {masked_number}"


def get_change_date(date: str) -> str:
    """Функция, которая принимает дату и изменяет ее"""
    change_date = date[0:10].split("-")
    return ".".join(change_date[::-1])
