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
        self.id = dict_["id"]
        self.state = dict_["state"] == "EXECUTED"
        self.date = dict_["date"]
        self.operationAmount = dict_["operationAmount"]
        self.description = dict_["description"]
        self.from_ = dict_["from"]
        self.to = dict_["to"]
        self.valid = self.validate()

    def validate(self) -> bool:
        return True

    def __repr__(self):
        return f"{self.id},"
