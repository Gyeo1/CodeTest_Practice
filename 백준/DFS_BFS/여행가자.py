#https://www.acmicpc.net/problem/1976 골드 4문제

from collections import deque

def dfs(start):
    global check,graph
    check[int(start)]=True
    for i in range(len(graph[start])):
        if check[graph[start][i]] == False:
            check[graph[start][i]]=True
            dfs(graph[start][i])
    return

city_num=int(input())
plan_city=int(input())
graph=[[] for _ in range(city_num+1)]
check=[False]*(city_num+1)

for i in range(1,city_num+1):
    city_info=((input().split()))
    for j in range(len(city_info)):
        if i==j:
            continue
        if city_info[j]=='1':
            graph[i].append(j+1)
            graph[j+1].append(i)
plan=deque(input().split())
dfs(int(plan[0]))
answer=0
for j in plan:
    if  check[int(j)]==True:
        answer+=1
if answer==plan_city:
    print("YES")
else:
    print("NO")
