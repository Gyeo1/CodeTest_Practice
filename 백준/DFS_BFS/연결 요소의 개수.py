# https://www.acmicpc.net/problem/11724 실버2
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline


def dfs(node):#확인할 노드
    global check,graph
    for i in range(len(graph[node])):
        next_node=graph[node][i]
        if check[next_node]==False:
            check[next_node]=True
            dfs(next_node)
    return

nodes, lines= map(int,input().split())
check=[False]*(nodes+1)
graph=[[] for _ in range(nodes+1)]
for _ in range(lines):
    node1,node2=map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
answer=0
for i in range(1,nodes+1):
    if check[i]==False:
        dfs(i)
        answer+=1
print(answer)
print(graph)