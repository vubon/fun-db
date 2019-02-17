import os
from src.FunDB import FunDB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

obj = FunDB(BASE_DIR + "/fun.db")


res = obj.get("c871a113-eed9-465e-99f6-5593d85e3edf")
print(res)
