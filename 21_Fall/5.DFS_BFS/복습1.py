from collections import deque
def dfs(graph, current_node, visited):
    visited[current_node]=True #현재 노드를 방문 처리
    print(current_node, end=" ")
    for i in graph[current_node]:
        if visited[i]==False:
            dfs(graph,i,visited) #재귀

def bfs(graph,current_node, visited):
    visited[current_node]=True
    queue=deque([current_node])
    while queue:
        a=queue.popleft()
        print(a,end=" ")
        for i in graph[a]: #실수한 부분 pop한걸 기준으로 해야되는데 현재 노드 기준으로 해버렸다.
            if visited[i]==False:
                queue.append(i)
                visited[i]=True

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
visited_bfs=[False]*len(graph)

dfs(graph,1,visited)
print("")
bfs(graph,1,visited_bfs)
