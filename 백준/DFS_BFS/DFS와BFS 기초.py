from collections import deque

nord,line,start=map(int, input().split())
graph=[]
for i in range(line):
    ip=[int(x) for x in input().split()]
    graph.append(ip)
# print(graph)

#dfs는 재귀와 스택이 핵심
def dfs(graph,idx,visited):
    stack1=deque()
    visited[idx]=True #현재 인덱스는 방문 완료를 뜻하는 True
    print(idx,end=" ")
    for i in range(len(graph)): #방문 가능한 정점을 모두 찾는다.
        if idx in graph[i]:
            for k in range(len(graph[i])):
                if graph[i][k] != idx:
                    stack1.append(graph[i][k])
    stack1=sorted(stack1) #방문 가능한 정점중 제일 작은 수를 가지는 노드를 찾기 위함.
    # print(stack1)
    for j in range(len(stack1)): #제일 작은 노드 부터 dfs 실행
        if not visited[stack1[j]]:
            dfs(graph,stack1[j],visited)


#bfs는 큐가 핵심이다.
def bfs(graph,idx,visited):
    queue = deque()
    queue.append(idx)
    while queue:
        check=[]
        idx=queue.popleft()
        print(idx, end=" ")
        visited[idx] = True
        for i in range(len(graph)):
            if idx in graph[i]:
                for j in range(len(graph[i])):
                    if graph[i][j] !=idx and (visited[graph[i][j]]==False):
                        check.append(graph[i][j])
                        visited[graph[i][j]]=True
                #여기까지
        check.sort()
        queue.extend(check)




#
visited=[False]*(nord+1)
dfs(graph,start,visited)
print()
visited=[False]*(nord+1)
bfs(graph,start,visited)