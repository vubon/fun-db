import os
from src.FunDB import FunDB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

obj = FunDB(BASE_DIR + "/fun.db")

# res = obj.get("caeaf9e6-ccc2-4f61-91ad-f384a3620881")
res = obj.get()
print(res)
