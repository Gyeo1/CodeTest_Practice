## template
N=int(input())
result=[int(x) for x in input().split()]
count=0
value=0
if 1<=N<=100:
  for i in range(N):
    if result[i]==0:
      count=0
    if result[i]==1:
      count+=1
      value+=count
  print(value)