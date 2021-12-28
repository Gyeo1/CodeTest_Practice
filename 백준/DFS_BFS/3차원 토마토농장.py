#토마토 문제에서 영향 범위가 상,하,좌,우, 위칸,아래칸 까지로 늘어남
from collections import deque
M,N,H=map(int,input().split()) #M,N은 상자의 크기, H는 쌓아진 상자 수
graph=[]
queue=deque()
stair,x,y=0,0,0
for _ in range(H):
    ip=[]
    for _ in range(N):
        ip.append(list(int(x) for x in input().split()))
    graph.append(ip)

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if 1 not in graph[i][j]:#1의 위치를 찾아라.
            continue
        for k in range(len(graph[i][j])):
            if graph[i][j][k]==1:
                queue.append([i,k,j]) #i번째 박스, x축 y축으로 저장


def bfs(queue):
    global stair,x,y
    while queue:
        stair,x,y=queue.popleft()
        if stair+1<H and graph[stair+1][y][x]==0:
            graph[stair + 1][y][x]=graph[stair][y][x]+1
            queue.append([stair+1,x,y])
        if (stair-1)>-1 and graph[stair-1][y][x]==0:
            graph[stair - 1][y][x]=graph[stair][y][x]+1
            queue.append([stair-1,x,y])
        if x + 1 < M and graph[stair][y][x + 1] == 0:
            graph[stair][y][x + 1] = graph[stair][y][x] + 1  # 현재 값 기준으로 +1 시킨 값을 넣어준다.
            queue.append([stair,x + 1, y])
        if (x - 1) > -1 and graph[stair][y][x - 1] == 0:
            graph[stair][y][x - 1] = graph[stair][y][x] + 1
            queue.append([stair,x - 1, y])
        if y + 1 < N and graph[stair][y + 1][x] == 0:
            graph[stair][y + 1][x] = graph[stair][y][x] + 1
            queue.append([stair,x, y + 1])
        if (y - 1) > -1 and graph[stair][y - 1][x] == 0:
            graph[stair][y - 1][x] = graph[stair][y][x] + 1
            queue.append([stair,x, y - 1])

bfs(queue)
# print(graph)

#모두 -1이면 익지 못할 상태니 -1출력
#모두 0이여도 익지못할 상태니 -1 출력
#모두 1이면 모두 익었으니 0
#그게 아니라면 이제 모든 곳을 돌아다니면서 0이 있다면 -1

#저장될때 부터 모든 토마토가 익었다면 0, 토마토가 모두 익지 못한 상태라면 -1출력
#처음부터 모든 값이 0이면? -1 출력인데 count=0이다.
max_val=0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        # print(graph[i][j],max(graph[i][j]))
        if max_val<(max(graph[i][j])):
            max_val=(max(graph[i][j]))
        if 0 in graph[i][j]:#만약 0인 부분이 있다? 그럼 못채워 진거니까 -1
            print(-1)
            exit()

if max_val >1:
    print(max_val-1)
elif max_val ==1 :
    print(0)
else:
    print(-1)