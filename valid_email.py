#write a pgm to tell if email address is valid 
def valid_email(e):
  check=0
  if e[0].isalpha()==False and e[0].isdigit()==False:
    return False
  l=len(e)
  if l>256:
    return False
  if '@' not in e:
    return False
  i=e.find('@',0,l)
  j=e.find('.',0,l)
  val=e[0:i]
  ans=e[i:j]
  k=e.rindex('.')
  last=e[k:l]
  if val=="" or ans=="" or last=="":
    return False
  return True
 
e=input("Enter the email address : ")
ans = valid_email(e)

if ans:
  print("The email address is valid")
else:
  print("The email address is invalid")