#신종 바이러스 웜 바이러스는 네트워크로 전파된다. 한 컴퓨터가 걸리면 네트워크상의 모든 컴퓨터는 바이러스가 걸림
from collections import deque
computer_number=int(input())
line_number=int(input())
graph=[]
start=1 #항상 시작은 1번 컴퓨터 부터 시작한다.
for i in range(line_number):
    ip=[int(x) for x in input().split()]
    graph.append(ip)


def bfs(graph,idx,visited):
    answer=0
    queue=deque()
    queue.append(idx)
    visited[idx]=True
    while queue:
        check=[]
        idx=queue.popleft()
        for i in range(len(graph)):
            if idx in graph[i]:
                for j in range(len(graph[i])):
                    if graph[i][j] !=idx and visited[graph[i][j]]!=True:
                        check.append(graph[i][j])
                        visited[graph[i][j]]=True
        answer+=len(check)
        queue.extend(check)
    return answer


visited=[False]*(computer_number+1)
answer=bfs(graph,start,visited)
print(answer)