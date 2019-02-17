import os
from src.FunDB import FunDB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

obj = FunDB(BASE_DIR + "/fun.db")

res = obj.get("93edeaaf-dc4e-4b06-ad2e-eb52188df836")
print(res)
