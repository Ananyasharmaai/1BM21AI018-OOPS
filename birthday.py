class birthdayboy():
  def __init__(self,name,age):
    self.n=name
    self.a=age
  def birthday(self,a):
    self.a+=1
    return self.a

name=input("Enter the name of the person: ")
age=int(input("Enter the age of the person : "))

ans=birthdayboy(name,age)

increased=ans.birthday(age)
print("The increased age is : ",increased)