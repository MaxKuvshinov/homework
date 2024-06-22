import logging
import os

log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
os.makedirs(log_dir, exist_ok=True)
logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
log_filename = os.path.join(log_dir, 'masks.log')
file_handler = logging.FileHandler(log_filename, mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
