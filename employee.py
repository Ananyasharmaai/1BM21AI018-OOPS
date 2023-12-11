class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.__salary=salary

  def work(self):
    print("The person working is :",self.name)
  def show(self):
    print("The name of the person is :",self.name,"and the salary is :",self.__salary)

emp=Employee("John",25000)
emp.work()
emp.show()