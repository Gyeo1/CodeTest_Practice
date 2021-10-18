#NxN 크기의 정사각형 공간 위에서 계획서가 주어졌을때 목적지 좌표를 출력하시오
import time
N=int(input())
Plan=list(input().split())
x=1
y=1
start_time = time.time()# 측정 시간
#L: 왼쪽한칸, R:오른쪽 한칸, U:위로 한칸, D: 아래로 한칸 이동.
if 1<=N<=100 and 1<len(Plan)<=100:
    for i in range(len(Plan)):
        if Plan[i] == "R":
            if y<N:
                y+=1
        elif Plan[i] == "L":
            if y>1:
                y-=1
        elif Plan[i] == "U":
            if x>1:
                x-=1
        elif Plan[i] == "D":
            if x < N:
                x += 1
print(x,y)



end_time=time.time()# 측정 종료
print("걸린시간은 ?:", end_time-start_time);
#아래 부분은 책에서 소개하는 방식이다. 마치 switch case 문처럼 이용하는 방법이다.

# N=int(input())
# Plan=(input().split())
# x,y=1,1
#
# #여기가 핵심 move_type에 따라 dx,dy를 정해준다 즉 move_type[0or1]이 L,R이기 때문에 L,R은 y만 움직이게 하므로
# #dy의 0,1번 인덱스에는 +-1이 들어가고 dx는 0만들어간다.
# dx=[0,0,-1,1] #x축을 이동하는 방식!
# dy=[-1,1,0,0] #y축을 이동하는 방식!
# move_type=['L','R','U','D']
#
# for i in Plan: #Plan의 문자를 받아온다.
#     for j in range(len(move_type)):
#         if i==move_type[j]:
#             # if x+dx[j]<N or x+dx[j]>1 or  y+dy[j] >1 or y+dy[j]<N:
#             nx=x+dx[j]
#             ny=y+dy[j]
#     if nx<1 or ny<1 or nx>N or ny>N: #여기가 범위를 벗어날 경우 x,y에 값을 안넣기 위해 사용한다.
#         continue
#     x,y=nx,ny
# print(x,y)