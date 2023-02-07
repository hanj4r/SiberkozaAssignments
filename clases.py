# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#220208905
#you can Create a class very easily
class User_ID:
  #creating a class using Constructor
  def __init__(self, name_ID, email_ID, age_ID):
    self.name_ID = name_ID
    self.email_ID = email_ID
    self.age_ID = age_ID

    # Encapsulating variables is added... Making variables inaccessible to child classes or only partially accessible to them is the idea behind encapsulation.
    self._private = 1500 # Encapsulated variables are defined with '_' in the constructor.

  def greeting(self):
      return f'My name is {self.name_ID} and I am {self.age_ID}'

  def has_birthday(self):
      self.age_ID += 1

 #a simple function for encap variable
  def print_encap(self):
      print(self._private)

# how to extend a class
class Customer(User_ID):
  # extending a class using Constructor
  # Called the appropriate parent class' constructor to create this as its rightful offspring, including all methods.
  def __init__(self, name_ID, email_ID, age_ID):
      User_ID.__init__(self, name_ID, email_ID, age_ID)
      self.name_ID = name_ID
      self.email_ID = email_ID
      self.age_ID = age_ID
      self.balance = 0

  def set_balance(self, balance):
      self.balance = balance

  def greeting(self):
      return f'My name_ID is {self.name_ID} and I am {self.age_ID} and my balance is {self.balance}'

#  Init user object
 peddy_ID = User_ID('peddy_ID Jeffery', 'peddy_Id@gmail.com', 59)
# Init customer object
eddy_ID = Customer('eddy_ID amanov', 'eddy_ID@outlook.com', 45)

eddy_ID.set_balance(500)
print(eddy_ID.greeting())

peddy_ID.has_birthday()
print(peddy_ID.greeting())

#Encapsulation -->
peddy_ID.print_encap()
peddy_ID._private = 800 #Changing for peddy_ID
peddy_ID.print_encap()

# Method of inherited from parent
eddy_ID.print_encap() #Changing the variable for peddy_ID doesn't have any affect on eddy_ID  variable --> Encapsulation
eddy_ID._private = 600
eddy_ID.print_encap()
#and the same goes for eddy_ID if we change it the peddy_ID will not be changed
peddy_ID.print_encap()
