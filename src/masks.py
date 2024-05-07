def mask_number_card(number_card: str) -> str:
    """Функция, которая возвращает маску карты"""
    masked_number = number_card[:4] + " " + number_card[4:6] + "** ****" + " " + number_card[-4:]
    return masked_number


def mask_account_number(account_number: str) -> str:
    """Функция, которая возвращает маску счета"""
    masks_account = "**" + account_number[-4:]
    return masks_account
