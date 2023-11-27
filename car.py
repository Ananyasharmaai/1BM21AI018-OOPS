#create a class called car that accepts 3 arguments, brand ,model and year. inititalize the class instance variable with the values supplied . display_car_details method is invoked using the class object and it is used to show the car details 
class car():
  def __init__(self,brand,model,year):
    self.model=model
    self.brand=brand
    self.year=year
  def display_car_details(self):
    print("Car brand is : ",self.brand)
    print("Car model is: ", self.model)
    print("The car was manufactured in :", self.year)

b=input("Enter the car brand :")
m=input("Enter the car model :")
y=int(input("Enter the year in which the car was manufactured :"))

v=car(b,m,y)
v.display_car_details()