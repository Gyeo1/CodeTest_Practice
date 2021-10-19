import time
N,M=map(int,input().split())
A,B,d=map(int,input().split())
Map=[]
history=[[0]*M for _ in range(N)] #이동 경로 저장용이다.
history[A][B]=1

for i in range(N):
    Map.append(list(map(int,input().split())))
start_time = time.time()# 측정 시간
dx=[-1,0,1,0]
dy=[0,1,0,-1] #순서대로 북 동 남 서이다 x축은 동/서만 확인한다

# Map[B][A]=1 Map은 건들지말고, history만 건들여라!

turn_count=0
count=1
while 1:
    #한번 회전 시키기
    d-=1
    if d==-1:
        d=3
    #회전 시킨 상태에서 좌표값 설저
    nx=dx[d]+A
    ny=dy[d]+B
    if Map[nx][ny] ==0 and history[nx][ny]==0: #이동 가능한 구역이면?
        #내가 헷갈림 부분! ==>and history 부분을 안넣어줬다. 이걸 넣어줘야 이동했던 경로를 제외할 수 있다.
        history[nx][ny] = 1  # 방문한 위치 저장.
        A=nx
        B=ny
        count+=1
        turn_count=0
        continue
    else:
        turn_count += 1
    if turn_count==4:
        nx=A-dx[d]
        ny=B-dy[d]
        if Map[nx][ny]==0:
            A=nx
            B=ny
        else:
            break
        turn_count=0
print(count)


end_time=time.time()# 측정 종료
print("걸린시간은 ?:", end_time-start_time);