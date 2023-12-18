class COMPLEX:
  def __init__(self,real_part,img_part):
    self.real_part=real_part
    self.img_part=img_part
  def addition(self,other):
    real=self.real_part+other.real_part
    img=self.img_part+other.img_part
    print("The addition of the two complex numbers is :",real,"+ i",img)

c1=COMPLEX(5,3)
c2=COMPLEX(2,4)
c3=c1.addition(c2)
