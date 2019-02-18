import json
from .create_obj import obj

res = obj.all()
print(json.dumps(res))
