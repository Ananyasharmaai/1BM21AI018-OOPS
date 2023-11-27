#create a default constructor for student class. the default constructor initializes name, age and grade attributes of the object to their default values 
class student():
  def __init__(self):
    self.name="John"
    self.age=24
    self.grade="B"
  def ans(self):
    print("The name is :",self.name)
    print("The age is :",self.age)
    print("The grade is :",self.grade)

s=student()
s.ans()