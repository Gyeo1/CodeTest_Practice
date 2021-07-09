## template.
N,S= map(int, input().split())
result=[]
if 1<=N<=100 and 1<=S<=9:
  for i in range(1,N+1):
    for j in range(N-i):
      print("",end=" ")
    for k in range(1,2*(i-1)+2):
      result.append(S)
      S+=1
      if S==10:
        S=1
    if i%2==0:
      for l in range(k):
        print(result[l],end="")
    else:
      result.reverse()
      for l in range(k):
        print(result[l],end="")
    result.clear()
    print("")
