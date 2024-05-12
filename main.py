from src.processing import get_dicts_by_state, sort_by_date
from src.widget import get_change_date, get_mask_account_card

print(get_mask_account_card("Visa Platinum 899092211366522"))

print(get_mask_account_card("Счет 73654108430135874305"))

print(get_change_date("2018-07-11T02:26:18.671407"))

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(get_dicts_by_state(data))

print(get_dicts_by_state(data, state="CANCELED"))

print(sort_by_date(data))
