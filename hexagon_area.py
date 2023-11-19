#write program to return area of hexagon by taking its side length
import math

def hexagon_area(a):
  area=3*math.sqrt(3)*(a**2)/2
  return area

a=int(input("Enter the side of the hexagon : "))

ans=hexagon_area(a)

print("The area of the hexagon is :",ans)