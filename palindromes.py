#pgm to take a string as input and return list of all palindromes in the string
def palindromes(s):
  ans=[]
  n=len(s)
  for i in range(n):
    for j in range(i+1,n+1):
      sub=s[i:j]
      if sub==sub[::-1]:
        ans.append(sub)
  return ans

s=input("Enter the string :")
ans=palindromes(s)
print("The palindromes found in the given string are: ",ans)