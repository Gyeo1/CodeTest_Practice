## template
'''
Colorpaper
순서
1)먼저 전체 평면을 0으로! 초기화 해준다 여기선 101*101의 평면이라 생각
2)들어 오는 입력 값에 대해서 0의 배열 값을 1로 바꿔준다. 즉 2차원 배열을 채워준다고 생각하자
3)다음으로 들어오는 값은 1에서 +1식 시켜준다 즉 처음 값은1로 다음 값은 2로 바꿔주면된다 그러면 겹치는 부분은 자연스래 사라진다
'''
N= int(input())
count=0
array1=[[0]*101 for _ in range(101)]
if 1<=N<=100:
  a=[[int(x) for x in input().split()] for i in range(N)]
  for i in range(N):
    if 0<=a[i][0]<101 and 0<=a[i][1]<101:
      count+=1
  if count==N:
    count=1
    for i in range(N):
      for j in range(a[i][3]):#세로
        for k in range(a[i][2]):#가로
          array1[((a[i][1])+j)][((a[i][0])+k)]=(i+1)
    for k in range(N):
      count=0
      for i in range(len(array1)):
        for j in range(len(array1[i])):
          if array1[i][j]==k+1:
            count+=1
      print(count)