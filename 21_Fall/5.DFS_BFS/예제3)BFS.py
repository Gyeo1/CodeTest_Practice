from  collections import deque

def bfs(graph,start,visited):
    visited[start]=True #방문 처리
    queue=deque([start]) #queue를 시작점이 들어간 상태로 초기화

    while queue: #큐가 존재 하면 계속 반복
        v=queue.popleft()
        print(v)
        for i in graph[v]: #인접한 노드들을 전부 i로 받아와서 append 시킨다.
            if visited[i]==False:
                queue.append(i)
                visited[i]=True

    #재귀 함수가 없다!


graph=[
    [],
    [2,3,8], #1번 노드는 2,3,8번 노드랑 이어져 있다란 의미이다.
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*len(graph)
