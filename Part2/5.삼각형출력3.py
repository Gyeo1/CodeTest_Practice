## template
n=int(input())
if 0<=n<=100:
  for j in range(n):
    for i in range(1,n-j):
      print("",end=" ")
    for k in range(1+2*j):
      print("*",end="")
    print("")