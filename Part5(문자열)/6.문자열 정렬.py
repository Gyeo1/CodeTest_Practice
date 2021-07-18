## template
n=int(input())
check=[]
save=[]
i=0
j=0
if 1<=n<=100:
  for i in range(n):
    a=input()
    if 1<=len(a)<=100:
      check.append(a)
    else:
      check.clear()
  if len(check)!=0:
    check.sort()
    for i in range(len(check)):
      print(check[i])