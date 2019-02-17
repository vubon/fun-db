import os
from src.FunDB import FunDB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

obj = FunDB(BASE_DIR + "/fun.db")

res = obj.delete("7dce8cdd-466d-44c4-b873-8d5897101cbf")
print(res)
