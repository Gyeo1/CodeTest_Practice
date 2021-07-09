## template
N= int(input())
column=1
row=1
for i in range(1,N+1):
  print(column,end=" ")
  for j in range(1,N-i+1):
    print(column+row,end=" ")
    row+=i+j
  print("")
  column+=i*2-i+1
  row=1+i