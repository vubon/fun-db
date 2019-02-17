import os
from src.FunDB import FunDB
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

obj = FunDB(BASE_DIR + "/fun.db")

one = obj.set("name",  "Vubon Roy")
print(one)
two = obj.set("Name", "Vubon Roy2")
print(two)
three = obj.set("Name", "Vubon Roy3")
print(three)
four = obj.set("Name", "Vubon Roy4")
print(four)
