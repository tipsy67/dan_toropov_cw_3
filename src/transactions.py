class Transactions:
    def __init__(self, dict_: dict):
        self.id = dict_["id"]
        self.state = dict_["state"] == "EXECUTED"
        self.date = dict_["date"]
        self.operationAmount = dict_["operationAmount"]
        self.description = dict_["description"]
        self.from_ = dict_["from"]
        self.to = dict_["to"]
        self.valid = self.validate()

    def validate(self) -> bool:
        pass
