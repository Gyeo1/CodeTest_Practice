## template
str1=input()
check=[]
if 1<=len(str1)<=1000:
  for i in range(len(str1)):
    check.append(str1[i])
  check.reverse()
  for i in range(len(check)):
    print(check[i],end="")