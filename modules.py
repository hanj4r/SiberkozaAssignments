#220208905 Muhammethanjar Nepesov
import datetime
from datetime import date
import time
from time import time
from camelcase import CamelCase
import validator
from validator import validate_email
today_ya = date.today()
timestamp_ya = time()
c_ID = CamelCase()
print(c_ID.hump('hello the new world'))
emailId = 'test#test.com'
if validate_email(emailId):
  print('Email is Correct')
else:
  print('Email is not correct')