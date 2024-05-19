import logging
import json
from datetime import datetime

from src.settings import QUANTITY_TRANSACTIONS, PATH_TO_OPERATIONS, PATH_TO_LOG, ERROR_LOG
from src.transactions import Transactions

logging.basicConfig(level=logging.ERROR,
                    filename=PATH_TO_LOG,
                    filemode='w',
                    format='%(asctime)s -%(name)s - %(levelname)s - %(message)s')

if not ERROR_LOG:
    logging.disable(logging.CRITICAL)


def load_json() -> [Transactions]:
    """
    загрузим транзакции
    :return:
    """
    with open(PATH_TO_OPERATIONS) as file:
        list_ = json.load(file)

    last_valid_trans = 0
    list_transactions = []

    for x in list_:
        try:
            transaction = Transactions(x)
            list_transactions.append(transaction)
        except KeyError as e:
            logging.error(f'missing key:{e} following the transaction id:{last_valid_trans}')
        except ValueError as e:
            logging.error(e)
        else:
            last_valid_trans = transaction.id

    return list_transactions


def return_last_trans(list_: [Transactions]) -> [Transactions]:
    """
    вернем последние транзакции в количестве QUANTITY_TRANSACTIONS
    :param list_:
    :return:
    """
    local_copy = list_[:]
    local_copy = [x for x in local_copy if x.state]
    local_copy = sorted(local_copy, key=lambda x: x.date, reverse=True)
    local_copy = local_copy[:QUANTITY_TRANSACTIONS]
    return local_copy


def format_acc_str(str_) -> str:
    """
    применим маску вывода на номер счета/карты
    :param str_:
    :return:
    """
    list_ = str_.split()
    str_ = list_[-1]
    if len(str_) == 16:
        list_[-1] = f"{str_[:4]} {str_[4:6]}** **** {str_[12:]}"
    elif len(str_) == 20:
        list_[-1] = f"**{str_[16:]}"
    return ' '.join(list_)


def format_trans(transaction: Transactions) -> str:
    """
    преобразуем транзакцию в строку вывода
    :param transaction:
    :return:
    """
    format_str = ""
    format_str += datetime.strftime(transaction.date, '%d.%m.%Y') + " "
    format_str += transaction.description + "\n"
    if transaction.from_maybe_empty is not None:
        format_str += format_acc_str(transaction.from_maybe_empty)
    format_str += " -> " + format_acc_str(transaction.to) + "\n"
    format_str += transaction.operationAmount["amount"] + " "
    format_str += transaction.operationAmount["currency"]["name"] + "\n"
    return format_str


def print_trans() -> None:
    """
    печать последних завершенных и валидных транзакций
    в количестве QUANTITY_TRANSACTIONS
    :return:
    """
    try:
        list_transactions = load_json()
    except FileNotFoundError as e:
        logging.error(e)
    except PermissionError as e:
        logging.error(e)
    else:
        list_transactions = return_last_trans(list_transactions)
        for x in list_transactions:
            print(format_trans(x))
