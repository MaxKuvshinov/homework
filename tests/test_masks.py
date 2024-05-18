import pytest

from src.masks import mask_number_card, mask_account_number

@pytest.mark.parametrize("number_card, masked_number",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_mask_number_card(number_card, masked_number):
    assert mask_number_card(number_card) == masked_number

@pytest.mark.parametrize("account_number, masks_account",
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_mask_account_number(account_number, masks_account):
    assert mask_account_number(account_number) == masks_account

