## template
str1=input()
check=[]
count=0
if 1<=len(str1)<=1000:
  for i in range(len(str1)):
    check.append(str1[i])
  check.reverse()
  for i in range(len(str1)):
    if check[i]==str1[i]:
      count+=1
    else:
      break
  if count == len(str1):
    print("YES")
  else:
    print("NO")