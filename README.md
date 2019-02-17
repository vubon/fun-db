# Fun DB(Fun Database)
This is a experimental database. This database behaviours like a NoSQL database.

## API List

| API name   | Status       |
| ---    | ---         | 
| Set   | `Done`       
| Delete  | `Done`      |
| Get    | `Done`       | 
| All   | `Done`       | 

## Futures List
| Futures name   | Status       |
| ---    | ---         | 
| Log collections    | `Done`       |  


## Uses
Set, Get, All, Delete Data from Fun DB 
```pythondoc
>>> from src.FunDB import FunDB
>>> obj = FunDB("./fun.db")
>>> obj.set('name', 'Vubon Roy')
'a38261c7-9be1-4c54-a053-736b0a03c358'
>>> obj.get('a38261c7-9be1-4c54-a053-736b0a03c358')
{'name': 'Vubon Roy'}

>>> obj.all()
{'66f32be9-417c-4fdb-8f95-c7bd08c24e81': {'name': 'Vubon Roy'},
 '3c124e7b-6998-45b3-96c8-9419a7d41f29': {'name': 'Vubon Roy'}}
 
>>> obj.delete('66f32be9-417c-4fdb-8f95-c7bd08c24e81')
True
>>> obj.all()
{'3c124e7b-6998-45b3-96c8-9419a7d41f29': {'name': 'Vubon Roy'}}

```
The return ID is a unique ID and by this ID we can get our data.
