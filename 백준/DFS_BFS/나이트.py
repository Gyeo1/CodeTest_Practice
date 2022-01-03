from collections import deque
N=int(input())

def bfs(start_point,end_point,graph):
    queue=deque()
    queue.append([start_point[1],start_point[0]])
    # graph[start_point[0]][start_point[1]]=1
    #나이트가 이동 가능한 구역? ==>상하좌우 *오왼 =8가지이다.
    while graph[end_point[1]][end_point[0]]==0:
        y,x=queue.popleft()
        #x관련 +-2일 경우
        if x+2<size and y+1<size and graph[y+1][x+2]==0:
            graph[y + 1][x + 2] =graph[y][x]+1
            queue.append([y+1,x+2])
        if x+2<size and (y-1)>-1 and graph[y-1][x+2]==0:
            graph[y - 1][x + 2] =graph[y][x]+1
            queue.append([y-1,x+2])
        if (x-2)>-1 and y+1<size and graph[y+1][x-2]==0:
            graph[y+1][x-2]=graph[y][x]+1
            queue.append([y+1,x-2])
        if (x-2)>-1 and y-1>-1 and graph[y-1][x-2]==0:
            graph[y-1][x-2]=graph[y][x]+1
            queue.append([y-1,x-2])
        #y관련 +-인경우
        if x+1<size and y+2<size and graph[y+2][x+1]==0:
            graph[y+2][x+1]=graph[y][x]+1
            queue.append([y+2,x+1])
        if (x-1)>-1 and y+2<size and graph[y+2][x-1]==0:
            graph[y+2][x-1]=graph[y][x]+1
            queue.append([y+2,x-1])
        if x+1<size and y-2>-1 and graph[y-2][x+1]==0:
            graph[y-2][x+1]=graph[y][x]+1
            queue.append([y-2,x+1])
        if x-1>-1 and y-2>-1 and graph[y-2][x-1]==0:
            graph[y-2][x-1]=graph[y][x]+1
            queue.append([y-2,x-1])
    print(graph[end_point[1]][end_point[0]])
for _ in range(N):
    size=int(input())
    graph=[[0 for i in range(size)] for j in range(size)]
    start_point=[int(x) for x in input().split()]
    #0 0 이렇게 된다 x,y를 나타냄
    end_point=[int(y) for y in input().split()]
    if start_point[0]==end_point[0] and start_point[1]==end_point[1]:
        print(0)
    else:
        bfs(start_point,end_point,graph)
    # print(start_point,end_point)