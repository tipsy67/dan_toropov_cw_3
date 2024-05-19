from datetime import datetime


class Transactions:
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
        # self.id = dict_["id"] if "id" in dict_ else self.missing_key("id")
        self.id = dict_["id"]
        self.state = dict_["state"] == "EXECUTED"
        self.date = datetime.strptime(dict_["date"], '%Y-%m-%dT%H:%M:%S.%f')
        self.operationAmount = dict_["operationAmount"]
        self.description = dict_["description"]
        self.to = dict_["to"]
        if "from" in dict_:
            self.from_maybe_empty: str = dict_["from"]
            self.validate(self.from_maybe_empty.split()[-1])
        else:
            self.from_maybe_empty = None
        self.validate(self.to.split()[-1])


    def validate(self, account: str) -> None:
        """
        дополнительная проверка валидности длины номера счета/карты
        :param account: строка с номером счета
        :return:
        """
        if not (account.isdigit and (len(account) == 16 or len(account) == 20)):
            raise ValueError(f'account error {account} in id:{self.id}')

    def __repr__(self):
        return f"{self.id} {self.date}"