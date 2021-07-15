## template
count1=0
count2=0
count3=0
row=0
col=0
a=[[int(x) for x in input().split()]for i in range(8)]
#1은 킹이다 2는 룩이다 3은 다른 기물(쫄) 킹은 한개만 룩은 2개 그외 기물은 29
for i in range(8):
  for j in range(8):
    if a[i][j]==1:
      count1+=1
      col=i
      row=j
    elif a[i][j]==2:
      count2+=1
    elif a[i][j]==3:
      count3+=1
if count1==1 and 0<=count2<=2 and 0<=count3<=29:
  count1=0
  #체스판의 인덱스는 0~7
  for i in range(col,0,-1):
    if a[i][row]==2:
      count1+=1
      break
    elif a[i][row]==3:
      break
  for j in range(col,8):
    if a[j][row]==2:
      count1+=1
      break
    elif a[j][row]==3:
      break
  for k in range(row,0,-1):
    if a[col][k]==2:
      count1+=1
      break
    elif a[col][k]==3:
      break
  for l in range(row,8):
    if a[col][l]==2:
      count1+=1
      break
    elif a[col][l]==3:
      break

  if count1!=0:
    print(1)
  else:
    print(0)