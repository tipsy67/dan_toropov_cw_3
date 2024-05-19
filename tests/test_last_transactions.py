import pytest

from src.last_transactions import format_acc_str, format_trans, print_trans
from src.transactions import Transactions

test_transaction = Transactions({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
})


@pytest.mark.parametrize("test_input,expected", [
    ("one two 12345678901234567890", "one two **7890"),
    ("one two 1234567890123456", "one two 1234 56** **** 3456")
])
def test_format_acc_str(test_input, expected):
    assert format_acc_str(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    (test_transaction,
     '26.08.2019 Перевод организации\n'
     'Maestro 1596 83** **** 5199 -> Счет **9589\n'
     '31957.58 руб.\n'
     ''),
])
def test_format_trans(test_input, expected):
    assert format_trans(test_input) == expected


# def test_print_trans():
#     assert print_trans() is None
