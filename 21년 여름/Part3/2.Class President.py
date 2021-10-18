N=int(input())
c=[]
result=[]
count=0
if 3<=N<=1000:
  for i in range(N):
    a=[int(x) for x in input().split()]
    c.append(a)
  for i in range(N):
    for j in range(5):
      if 1<=c[i][j]<=9:
        count+=1
  if count==N*5:
    for i in range(N):
      count=0
      for j in range(N):
        for k in range(5):
          if i!=j and c[i][k]==c[j][k]:
            count+=1
            break
      result.append(count)
  for i in range(N):
    if result[i]==max(result):
      print(i+1)
      break