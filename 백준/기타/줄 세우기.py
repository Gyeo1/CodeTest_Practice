#https://www.acmicpc.net/problem/2252 골드3
from collections import deque

N,M =map(int,input().split()) #N은 학생수, M은 비교수
# check=set()
check=deque()
graph=[[] for _ in range(N+1)]
for _ in range(M):
    low,high=map(int,input().split())
    graph[low].append(high)
    graph[high].append(low)
    # check.add(a)
    # check.add(b)

# print(check)
print(graph)
