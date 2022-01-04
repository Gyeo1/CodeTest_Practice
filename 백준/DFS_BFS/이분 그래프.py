import sys
from collections import deque
input=sys.stdin.readline
test_case=int(input())
def bfs(graph):
    keys=sorted(list(graph.keys()))
    start=keys[0] # 맨 첫번째 값을 가져옴.
    queue=deque()
    queue.append(start)
    left_side=[]
    rigth_side=[]
    left_side.append(start)
    visited=[False]*(node+1)
    while queue:
        idx=queue.popleft()
        print(idx,end=" ")
        visited[idx]=True
        for i in graph[idx]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True




for _ in range(test_case):
    node,lines=map(int,input().split())
    graph={}
    #인접 리스트 방식으로 graph 구현
    for _ in range(lines):
        x,y=map(int,input().split())
        if x not in graph.keys():
            graph[x]=set([y])
        else:
            graph[x].add(y)
        if y not in graph.keys():
            graph[y]=set([x])
        else:
            graph[y].add(x)
    print(graph)
    for i in graph.keys():
        print(i)
    bfs(graph)
