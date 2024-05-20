import datetime
from datetime import time

import pytest

from src.last_transactions import format_acc_str, format_trans, print_trans, load_json, return_last_trans
from src.transactions import Transactions

@pytest.fixture()
def test_transaction():
    return Transactions({
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

@pytest.fixture()
def test_transaction_from():
    return Transactions({
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
    "to": "Счет 64686473678894779589"
})


@pytest.mark.parametrize("test_input,expected", [
    ("one two 12345678901234567890", "one two **7890"),
    ("one two 1234567890123456", "one two 1234 56** **** 3456")
])
def test_format_acc_str(test_input, expected):
    assert format_acc_str(test_input) == expected


def test_format_trans(test_transaction):
    expected = '26.08.2019 Перевод организации\n'\
    'Maestro 1596 83** **** 5199 -> Счет **9589\n'\
    '31957.58 руб.\n'\
    ''
    assert format_trans(test_transaction) == expected

def test_load_json():
    assert isinstance(load_json(), list)

def test_return_last_trans():
    assert isinstance(return_last_trans(load_json()), list)

# test methods of class
def test_transaction_repr(test_transaction):
    print(str(test_transaction))
    assert str(test_transaction) == '441945886 2019-08-26 10:50:58.294041'

@pytest.mark.parametrize('test_input',["asasas", "11111"])
def test_transaction_validate(test_input,test_transaction):
    with pytest.raises(ValueError):
        test_transaction.validate(test_input)

def test_transaction_init(test_transaction_from):
    assert isinstance(test_transaction_from.date, datetime.datetime)
    assert test_transaction_from.from_maybe_empty is None




