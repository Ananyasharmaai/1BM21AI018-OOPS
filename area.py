#create parameterized constructor for rectangle class that takes two arguments length and breadth and initializes the length and breadth attributes of the object with the values passed as arguments 
class area():
  def __init__(self, l,b):
    self.l=l
    self.b=b
  def cal(self):
    a=self.l*self.b
    print("The area is :",a)
l=int(input("Enter the length of the rectangle :"))
b=int(input("Enter the breadth of the rectangle :"))
s=area(l,b)
s.cal()