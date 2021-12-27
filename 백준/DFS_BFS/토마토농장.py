#문제 M,N크기의 격자가 있다고 할때 1은 익은 토마타, 0은 안익은 토마토 -1은 익을 수 없는 토마토다.
#1 토마토는 상하좌우를 지나가면서 0인 구역을 1로만들어 준다.
from collections import deque
M,N=map(int,input().split())
graph=[]
check=[]
count=0
for _ in range(N):
    graph.append([int(x) for x in input().split()])
for i in range(len(graph)):
    if 1 not in graph[i]:
        continue
    for j in range(len(graph[i])):
        if graph[i][j]==1:
            check.append([i,j])

def bfs(check):
    global count
    queue=deque()
    for i in check:
        y,x=i
        queue.append([x,y])
    while queue:
        x,y=queue.popleft()
        if x + 1 < M and graph[y][x + 1] == 0:
            graph[y][x + 1] = graph[y][x] + 1  # 현재 값 기준으로 +1 시킨 값을 넣어준다.
            queue.append([x + 1, y])
            count+=1
        if (x - 1) > -1 and graph[y][x - 1] == 0:
            graph[y][x - 1] = graph[y][x] + 1
            queue.append([x - 1, y])
            count+=1
        if y + 1 < N and graph[y + 1][x] == 0:
            graph[y + 1][x] = graph[y][x] + 1
            queue.append([x, y + 1])
            count+=1
        if (y - 1) > -1 and graph[y - 1][x] == 0:
            graph[y - 1][x] = graph[y][x] + 1
            queue.append([x, y - 1])
            count+=1
bfs(check)
max_val=0
for i in range(len(graph)):
    if max(max(graph))==0:#처음 부터 그래프가 0으로 채워져있다면 익을수 없으니 -1출력
        print(-1)
        exit()
    if count==0:    #count가 0이라면 모두 1이나 -1로 채워져있다는 의미이므로 다 익은 상태라는 거다
        print(0) 
        exit()
    if 0 in graph[i]: #만약 0이 graph에 있다면 못익은게 하나 있으니깐 -1 출력
        print(-1)
        exit()
    #위의 모든 상황이 아니라면 최대 몇일이 걸렸는지 체크해라
    if max_val<max(graph[i]):
        max_val=max(graph[i])
print(max_val-1)