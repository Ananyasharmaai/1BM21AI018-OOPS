class Student:
  pass

class Marks(Student):
  pass

s=Student()
m=Marks()
print("Student object of student class :",isinstance(s,Student))
print("Marks object of Marks class :",isinstance(m,Marks))
print("Student object of marks class :",isinstance(s,Marks))
print("Marks object of student class :",isinstance(m,Student))

print("Marks subclass of student class :",issubclass(Marks,Student))