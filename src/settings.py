from pathlib import Path

PATH = Path(__file__).parent
PATH_TO_OPERATIONS = PATH.joinpath("data","operations.json")

ERROR_LOG = True # флаг для ведения строки ошибок в объекте Transactions

QUANTITY_TRANSACTIONS = 5 # количество возращаемых транзакций