from collections import deque
#bfs로 현재 노드는 이동한 칸수로 바꾸면서 이동하면된다!
N,M=map(int,input().split()) #N *M의 행렬 생성
graph=[]
for i in range(N):
    graph.append(list(int(x) for x in input()))

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    while queue:
        x,y=queue.popleft()
        if x+1<M and graph[y][x+1] ==1:
            graph[y][x+1]=graph[y][x]+1 #현재 값 기준으로 +1 시킨 값을 넣어준다.
            queue.append([x+1,y])
        if (x-1)>-1 and graph[y][x-1]==1:
            graph[y][x - 1] = graph[y][x] + 1
            queue.append([x-1,y])
        if y+1<N and graph[y+1][x]==1:
            graph[y+1][x] = graph[y][x] + 1
            queue.append([x, y+1])
        if (y-1)>-1 and graph[y-1][x]==1:
            graph[y-1][x] = graph[y][x] + 1
            queue.append([x, y-1])



bfs(0,0)
print(graph[N-1][M-1])