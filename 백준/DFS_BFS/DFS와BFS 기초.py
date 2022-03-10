from collections import deque

nord,line,start=map(int, input().split())
graph=[]
for i in range(line):
    ip=[int(x) for x in input().split()]
    graph.append(ip)


#dfs는 재귀와 스택이 핵심
def dfs(graph,idx,visited):
    stack1=deque()
    visited[idx]=True   #현재 인덱스는 방문 완료를 뜻하는 True
    print(idx,end=" ")
    for i in range(len(graph)):     #방문 가능한 정점을 모두 찾는다.
        if idx in graph[i]:
            for k in range(len(graph[i])):
                if graph[i][k] != idx:
                    stack1.append(graph[i][k])
    stack1=sorted(stack1)   #방문 가능한 정점중 제일 작은 수를 가지는 노드를 찾기 위함.

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

visited=[False]*(nord+1)
dfs(graph,start,visited)
print()
visited=[False]*(nord+1)
bfs(graph,start,visited)


# #아래는 BFS를 더 쉽게 하는 방법임!!
# from collections import deque
# import sys
# input=sys.stdin.readline
# def bfs(graph): #걍 첫번째 노드를 1이라 생각하자.
#     queue=deque()
#     queue.append(3)
#     visited=[False]*(node+1)
#     while queue:
#         idx=queue.popleft()
#         print(idx,end=" ")
#         visited[idx]=True
#         for i in range(len(graph[idx])):
#             if graph[idx][i]==1 and visited[i]==False:
#                 queue.append(i)
#                 visited[i]=True

#
#
#     # return
#
# node,lines=input().split()
# node=int(node)
# lines=int(lines)
# graph=[[0]*(node+1) for _ in range(node+1)]#이거랑
# for i in range(lines):
#     a,b=map(int,input().split())
#     graph[a][b]=graph[b][a]=1 #이게 핵심임 그냥
# #코드의 해석: 일단 graph를 node갯수 +1 개 만큼 만듬 이때 graph[0]은 안쓰기 때문에 +1개만큼만듬
# #간선의 정보를 입력받음 a,b로 받고 graph의 [a][b]를 1로 만든다 이때 1은 그냥 둘이 이어져있다는 것을 의미함
#
# bfs(graph)