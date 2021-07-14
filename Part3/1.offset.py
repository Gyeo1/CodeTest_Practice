
N=[[int(x) for x in input().split()],
[int(x) for x in input().split()],
[int(x) for x in input().split()],
[int(x) for x in input().split()],
[int(x) for x in input().split()]]
check=[]
for i in range(5):
  for j in range(5):
    if i==0:#맨 윗줄
      if j==0:
        if N[i][j]<N[i+1][j] and N[i][j]<N[i][j+1]:
          check.append([i,j])
      elif j==4:
        if N[i][j]<N[i+1][j] and N[i][j]<N[i][j-1]:
          check.append([i,j])
      else:
        if N[i][j]<N[i+1][j] and N[i][j]<N[i][j-1] and N[i][j]<N[i][j+1]:
         check.append([i,j])

    elif i==4:#맨 아랫줄
      if j==0:
        if N[i][j]<N[i-1][j] and N[i][j]<N[i][j+1]:
          check.append([i,j])
      elif j==4:
        if N[i][j]<N[i-1][j] and N[i][j]<N[i][j-1]:
          check.append([i,j])
      else:
        if N[i][j]<N[i-1][j] and N[i][j]<N[i][j-1]and N[i][j]<N[i][j+1]:
          check.append([i,j])

    else:#맨위 아래가 아닐경우
      if j==0:
        if N[i][j]<N[i-1][j]and N[i][j]<N[i+1][j]and N[i][j]<N[i][j+1] :
          check.append([i,j])
      elif j==4:
        if N[i][j]<N[i-1][j]and N[i][j]<N[i+1][j]and N[i][j]<N[i][j-1] :
          check.append([i,j])
      else:
        if N[i][j]<N[i-1][j]and N[i][j]<N[i+1][j]and N[i][j]<N[i][j-1] and N[i][j]<N[i][j+1]:
          check.append([i,j])
    #맨위 아래 빼고는 상하 좌우 확인이 가능 맨위는 하좌우, 맨 아래는 상좌우만 확인
    #그리고 맨오른쪽 왼쪽은 좌, 우가 없다.
for i in range(len(check)):
    a=check[i][0]
    b=check[i][1]
    N[a][b]='*'
print(N)