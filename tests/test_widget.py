import pytest

from src.widget import get_mask_account_card, get_change_date


@pytest.mark.parametrize("card_or_account, masking_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_get_mask_account_card(card_or_account, masking_result):
    assert get_mask_account_card(card_or_account) == masking_result


@pytest.mark.parametrize("date, result",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.4255722", "30.06.2018"),
    ],
)
def test_get_change_date(date, result):
    assert get_change_date(date) == result

