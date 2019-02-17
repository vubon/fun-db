import os
from src.FunDB import FunDB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

obj = FunDB(BASE_DIR + "/fun.db")

res = obj.get("5f60419d-80dc-48cc-a680-dc1d3663d24c")
print(res)
