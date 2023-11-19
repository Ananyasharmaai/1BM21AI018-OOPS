#write a python program to find largest element in list
def largest_ele(l):
  largest=l[0]
  for i in l:
    if i>largest:
      largest=i
  return largest

l=eval(input("Enter the list of elements :"))
ans=largest_ele(l)

print("The largest element is",ans)
