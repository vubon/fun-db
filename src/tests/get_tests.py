import os
from src.FunDB import FunDB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

obj = FunDB(BASE_DIR + "/fun.db")


res = obj.get("008b10d9-f4cd-40c6-b407-15b965727a04")
print(res)
