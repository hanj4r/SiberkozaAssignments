
#220208905 Muhammethanjar Nepesov

class userId:
  def __init__(self, nameId, emailId, ageId):
    self.nameId = nameId
    self.emailId = emailId
    self.ageId = ageId

    self._private = 1500 

  def greeting(self):
      return f'My name is {self.nameId} and I am {self.ageId}'

  def has_birthday(self):
      self.ageId += 1

  def print_encap(self):
      print(self._private)

class Customer(User-Id):
  def __init__(self, nameId, emailId, ageId):
      User-Id.__init__(self, nameId, emailId, ageId)
      self.nameId = nameId
      self.emailId = emailId
      self.ageId = ageId
      self.balance = 0

  def setBalance(self, balance):
      self.balance = balance

  def greeting(self):
      return f'My nameId is {self.nameId} and I am {self.ageId} and my balance is {self.balance}'

 dvltId = UserId('dvltId Jeffery', 'dvltId@gmail.com', 59)
hanjarId = Customer('hanjarId amanov', 'hanjarId@outlook.com', 45)

hanjarId.setBalance(500)
print(hanjarId.greeting())

dvltId.has_birthday()
print(dvltId.greeting())

dvltId.print_encap()
dvltId._private = 800 
dvltId.print_encap()

hanjarId.print_encap() 
hanjarId._private = 600
hanjarId.print_encap()
dvltId.print_encap()
