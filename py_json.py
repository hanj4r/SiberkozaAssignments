#220208905 Muhammethanjar Nepesov
import json
JsonId = '{"firstName": "Hanjar", "lastName": "Nepesov", "age": 22}'
userId = json.loads(JsonId)
carId = {'make': 'Ford', 'model': 'Explerer', 'year': 2017}
carJsonId = json.dumps(carId)
print(carJsonId)
