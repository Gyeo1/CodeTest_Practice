## template
import sys
a=[]
c=[]
d=[]
bingo=0
count=0
row=[]
cross1=[]
cross2=[]
for i in range(5):
  b=[int(x) for x in input().split()]
  c.append(b)
for j in range(5):
  b=[int(x) for x in input().split()]
  for i in range(5):
    a.append(b[i])
  d.append(b)
for i in range(5):
  for j in range(5):
    for k in range(5):
      for l in range(5):
        if c[i][j]==c[k][l]:
          count+=1
        if d[i][j]==d[k][l]:
          count+=1

if count ==50:
  for k in range(len(a)):
    if bingo>=3:
      print(k)
      break
    for i in range(5):
      for j in range(5):
        if a[k]==c[i][j]:
          c[i][j]=0
          cross1.clear()
          cross2.clear()
          bingo=0
          for n in range(5):
            cross1.append(c[4-n][n])
            cross2.append(c[n][n])
            row.clear()
            for m in range(5):
              row.append(c[m][n])
            if max(c[n])==0:
              bingo+=1
            if max(row)==0:
              bingo+=1
           # print(c[n])
          if max(cross1)==0:
            bingo+=1
          if max(cross2)==0:
            bingo+=1