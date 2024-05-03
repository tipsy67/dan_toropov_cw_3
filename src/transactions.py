import json

from src.settings import PATH_TO_OPERATIONS


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
        self.id = dict_["id"] if "id" in dict_ else ""
        self.state = dict_["state"] == "EXECUTED" if "state" in dict_ else False
        self.date = dict_["date"] if "date" in dict_ else ""
        self.operationAmount = dict_["operationAmount"] if "operationAmount" in dict_ else ""
        self.description = dict_["description"] if "description" in dict_ else ""
        self.from_ = dict_["from"] if "from" in dict_ else ""
        self.to = dict_["to"] if "to" in dict_ else ""
        self.valid = self.validate()

    def validate(self) -> bool:
        return True

    def __repr__(self):
        return f"{self.id} {self.date}"


def load_json() -> [Transactions]:
    with open(PATH_TO_OPERATIONS) as file:
        list_ = json.load(file)
    return [Transactions(x) for x in list_ if x != {}]


d = load_json()
print(d)
