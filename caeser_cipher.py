#program that takes string and integer and encrypts the text using caesar cypher
def caesar_cypher(t,s):
  res=""
  for i in t:
    if i.isupper():
      res+=chr((ord(i)+s-65)%26+65)
    else:
      res+=chr((ord(i)+s-97)%26+97)
  return res

t=input("Enter the text to be encrypted : ")
s=int(input("Enter the shift value : "))
a=caesar_cypher(t,s)
b=caesar_cypher(a,26-s)
print("The encrypted text is : ",a)
print("The decrypted text is : ",b)