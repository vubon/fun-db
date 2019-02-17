import os
from src.FunDB import FunDB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

obj = FunDB(BASE_DIR + "/fun.db")

res = obj.delete("eca73213-b3fa-41fa-ae34-c2f0662a3491")
print(res)
