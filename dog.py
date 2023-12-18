class Dog:
  def __init__(self,name,size,breed='unknown',dob='unknown'):
    self.__name=name
    self.size=size
    self.breed=breed
    self.dob=dob
  def bark(self):
    print("woof!")
  def get_name(self):
    print("The dog's name is :",self.__name)
  def set_name(self,new_name):
    if(len(new_name)>30 or len(new_name)<2):
      print("Invalid name")
    else:
      self.__name=new_name.title()
  def dog_years(self,age):
    print("The dog's age is :",7*age)

d=Dog('Toby',22)
d.bark()
d.get_name()
print(d._Dog__name)
d.set_name('daisy')
d.get_name()
d.dog_years(5)
