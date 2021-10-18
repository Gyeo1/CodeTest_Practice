## template
#문제 해석
# 옆으로 이동할때 늘어나는 값이 +1씩 늘어남
# 한줄이 늘어날때 마다 시작값이 이전줄 보다 순차적으로 늘어남
# 옆으로 이동하는 값은 한줄이 늘어날때 마다 시작값이 +1씩 늘어남

N= int(input())
column=1#맨처음으로 시작하는 값임
row=1# 가로 방향으로 더해지는 값임
#첫번째 for문은 줄의 갯수 두번째 for문은 줄에서 더해지는 값과 연관됨
for i in range(1,N+1):
  print(column,end=" ")
  for j in range(1,N-i+1):
    print(column+row,end=" ")
    row+=i+j#더해지는 값이 i 기준으로 1씩 증가함.
  print("")
  column+=i*2-i+1#각 줄에 맨 처음으로 나오는 값은 1,3,6,10~~ 이 값이 나오도록 하는 수식이다.
  row=1+i