# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
#220208905

# the core modules
import datetime
from datetime import date
import time
from time import time
# using pip  module
from camelcase import CamelCase

# Importing your own custom module
import validator
from validator import validate_email

#today = datetime.date.today()
today_ya = date.today()
timestamp_ya = time()

c_ID = CamelCase()
print(c_ID.hump('hello the new world'))

email_ID = 'test#test.com'
if validate_email(email_ID):
  print('Email is Correct')
else:
  print('Email is not correct')