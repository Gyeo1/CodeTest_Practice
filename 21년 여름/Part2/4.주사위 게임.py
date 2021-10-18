## template
N=int(input())
result=0
b=[]
c=[]
if 2<=N<=1000:
  for i in range(N):
    a=[int(x) for x in input().split()]
    b.append(a)#a로 받은 값을 b 리스트에 넣는다.
  for j in range(N):
    if b[j][0]==b[j][1]==b[j][2]:
        c.append(b[j][1]*1000+10000)
    elif b[j][0] ==b[j][1]:
        c.append((b[j][0])*100+1000)
    elif  b[j][0] ==b[j][2]:
        c.append((b[j][0]) * 100 + 1000)
    elif b[j][1] ==b[j][2]:
        c.append((b[j][1]) * 100 + 1000)
    else:
        c.append(max(b[j])*100)
  print(max(c))