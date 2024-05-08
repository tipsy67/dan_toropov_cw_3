from datetime import datetime

from src.settings import ERROR_LOG


class Transactions:

    is_trans_valid = True # флаг для отслеживания валидности транзакций
    err_str = "" # строка для хранения ошибок валидности при установленном ERROR_LOG

    def __init__(self, dict_: dict):
        """
        :param dict_:
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
        """
        self.id = dict_["id"] if "id" in dict_ else self.missing_key("id")
        self.state = dict_["state"] == "EXECUTED" if "state" in dict_ else self.missing_key("state")
        self.date = datetime.strptime(dict_["date"], '%Y-%m-%dT%H:%M:%S.%f') \
            if "date" in dict_ else self.missing_key("date")
        self.operationAmount = dict_["operationAmount"] if "operationAmount" in dict_ else self.missing_key("opAm")
        self.description = dict_["description"] if "description" in dict_ else self.missing_key("descr")
        self.from_maybe_empty: str = dict_["from"] if "from" in dict_ else None
        self.to = dict_["to"] if "to" in dict_ else self.missing_key("to")
        if self.from_maybe_empty is not None:
            self.validate(self.from_maybe_empty.split()[-1])
        self.validate(self.to.split()[-1])

    def missing_key(self, key: str) -> None:
        """
        для записи отсутвующего ключа в строку ошибок
        и сбрасывания флага валидности
        :param key: отсутствующий ключ в словаре тразакции
        :return:
        """
        if ERROR_LOG:
            self.err_str = self.err_str + "mis_" + key + ";"
        self.is_trans_valid = False

    def validate(self, account: str) -> None:
        """
        дополнительная проверка правильности длины номера счета\карты
        :param account: строка с номером счета
        :return:
        """
        if not (account.isdigit() and (len(account) == 16 or len(account) == 20)):
            self.is_trans_valid = False
            if ERROR_LOG:
                self.err_str = self.err_str + "ERR_ACC:"

    def __repr__(self):
        return f"{self.id} {self.date}" if self.is_trans_valid else self.err_str



