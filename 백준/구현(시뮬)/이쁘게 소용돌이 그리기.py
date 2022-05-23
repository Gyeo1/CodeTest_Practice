#https://www.acmicpc.net/problem/1022 골드 4


#소용돌이(달팽이)문제이다.

r1,c1,r2,c2= map(int,input().split())
#r1,r2는 각각 행(y축)이고 c1,c2는 열(x 축)이다.
x,y=0,0
direct=0
dx=[1,0,-1,0]
dy=[0,-1,0,1]

check=[[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

loop=1 # 1부터 시작해 1->1->2->2-> ... 계속 나아간다
current=(r2-r1+1)*(c2-c1+1) #check에 최대로 넣을 수 있는 수이다.
start=1

if r1 <= y <= r2 and c1 <= x <= c2:  # -3<=y<=2 && -3<=x<=0
    # print(y, x, start)  # 0,0 -> 0,1 -> -1,1 ->-1,0
    current -= 1
    check[y - r1][x - c1] = start
    max_num = start
while current>0:
    for i in range(loop):
        x+=dx[direct]
        y+=dy[direct]
        start+=1
        if r1<=y<=r2 and c1<=x<=c2: # -3<=y<=2 && -3<=x<=0
            # print(y, x, start)  # 0,0 -> 0,1 -> -1,1 ->-1,0
            current-=1
            check[y-r1][x-c1]=start
            max_num=start

    direct=(direct+1)%4
    if direct%2==0:
        loop+=1

max_num_len=len(str(max_num))
# print(max_num_len)
for i in range(len(check)):
    for j in range(len(check[i])):
        for k in range(max_num_len-len(str(check[i][j]))):
            print(" ",end="")
        print(check[i][j],end=" ")
    print("")
