from pathlib import Path

PATH = Path(__file__).parent
PATH_TO_OPERATIONS = PATH.joinpath("data","operations.json")
PATH_TO_LOG = PATH.joinpath("data","app.log")

ERROR_LOG = True # флаг для ведения лога

QUANTITY_TRANSACTIONS = 5 # количество возращаемых транзакций