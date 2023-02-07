# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

#220208905
#first we need to import json in order for it to work
import json

#  a basic JSON example
userJSON_ID = '{"first_name": "Peddy", "last_name": "Jeffery", "age": 23}'

# Parse to a dictionary
user_ID = json.loads(userJSON_ID)

 #print(user_ID)
 #print(user['first_name'])

car_ID = {'make': 'Ferrari', 'model': 'BX2', 'year': 2010}

carJSON_ID = json.dumps(car_ID)

print(carJSON_ID)
