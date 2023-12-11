class CreditCard:
  def __init__(self):
    self.__balance=0
    self.__limit=10000

  def get_balance(self):
    return self.__balance

  def withdraw(self,amount):
    if amount>self.__limit:
      print("Amount is exceeding the limit. Withdraw a lesser amount")
    if amount<=0:
      print("Withdraw a positive amount")
    if self.__balance<amount:
      print("Insufficient balance")
    else:
      self.__balance-=amount
      print("Withdrawn amount:",amount,"Remaining balance:", self.__balance)
      
  def deposit(self,amount):
    self.__balance+=amount
    print("Deposited amount:", amount, "Current balance:",self.__balance)

cc=CreditCard()
cc.deposit(1000)
cc.deposit(2000)
cc.withdraw(500)
cc.deposit(1500)
cc.withdraw(9000)