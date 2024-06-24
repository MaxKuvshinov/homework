from src.masks import mask_account_number, mask_number_card



def get_mask_account_card(card_or_account: str) -> str:
    """Функция, которая принимает номер карты или счета и маскирует"""

    if not isinstance(card_or_account, str):
        return card_or_account

    masking_result = ""
    words = card_or_account.split()
    number = words[-1]
    description = " ".join(words[:-1])

    if number.isdigit():
        if 13 <= len(number) <= 19:
            masked_number = mask_number_card(number)
        elif len(number) == 20:
            masked_number = mask_account_number(number)
        else:
            return card_or_account
    else:
        return card_or_account

    masking_result = f"{description} {masked_number}"

    return masking_result


def get_change_date(date: str) -> str:
    """Функция, которая принимает дату и изменяет ее"""
    result = ""
    change_date = date[0:10].split("-")
    result = ".".join(change_date[::-1])
    return result
