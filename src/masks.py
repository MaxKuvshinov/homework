from masks_logger_config import logger


def mask_number_card(number_card: str) -> str:
    """Функция, которая возвращает маску карты"""
    logger.info(f"Маскирование номера карты {number_card}")
    masked_number = number_card[:4] + " " + number_card[4:6] + "** ****" + " " + number_card[-4:]
    logger.info(f"Возврат маскированной карты: {masked_number}")
    return masked_number


def mask_account_number(account_number: str) -> str:
    """Функция, которая возвращает маску счета"""
    logger.info(f"Маскирование номера счета {account_number}")
    masks_account = "**" + account_number[-4:]
    logger.info(f"Возврат маскированного счета: {masks_account}")
    return masks_account
