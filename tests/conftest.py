from typing import Any, Dict, List

import pytest


@pytest.fixture
def masking_result() -> List[str]:
    return [
        "Maestro 1596 83** **** 5199",
        "**9589",
        "MasterCard 7158 30** **** 6758",
        "**5560",
        "Visa Classic 6831 98** **** 7658",
        "Visa Platinum 8990 92** **** 5229",
        "Visa Gold 5999 41** **** 6353",
        "**4305",
    ]


@pytest.fixture
def data() -> List[str]:
    return [
        "11.07.2018",
        "03.07.2019",
        "30.06.2018",
    ]


@pytest.fixture
def masked_number() -> List[str]:
    return [
        "7000 79** **** 6361",
        "7158 30** **** 6758",
        "6831 98** **** 7658",
        "8990 92** **** 5229",
        "5999 41** **** 6353",
    ]


@pytest.fixture
def masks_account() -> List[str]:
    return ["**4305", "**9589", "**5560", "**4305"]


@pytest.fixture
def sorted_list() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
