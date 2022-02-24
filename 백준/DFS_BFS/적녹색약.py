#https://www.acmicpc.net/problem/10026 골드5
import sys

sys.setrecursionlimit(10**6)
def dfs(color,y,x):#일반인용 dfs
    global graph_1
    graph_1[y][x]='0'
    if x+1<N and graph_1[y][x+1]==color:
        dfs(color,y,x+1)
    if x-1>=0 and graph_1[y][x-1]==color:
        dfs(color,y,x-1)
    if y+1<N and graph_1[y+1][x]==color:
        dfs(color,y+1,x)
    if y-1>=0 and graph_1[y-1][x] ==color:
        dfs(color,y-1,x)

def dfs2(color,y,x):#적녹 색맹용 dfs
    global graph_2
    graph_2[y][x]='0'   
    if x+1<N and graph_2[y][x+1]==color:
        dfs2(color,y,x+1)
    if x-1>=0 and graph_2[y][x-1]==color:
        dfs2(color,y,x-1)
    if y+1<N and graph_2[y+1][x]==color:
        dfs2(color,y+1,x)
    if y-1>=0 and graph_2[y-1][x] ==color:
        dfs2(color,y-1,x)


N=int(input())
graph_1=[[] for _ in range(N)]
graph_2=[[] for _ in range(N)]
for i in range(N):
    a=input()
    for j in a:
        graph_1[i].append(j)
        if j=="R":
            graph_2[i].append("G")
            continue
        graph_2[i].append(j)
# print(graph_1)
# print(graph_2)
count=0
for k in ['R','G','B']:
    for l in range(len(graph_1)):
        while 1:
            if k in graph_1[l]:
                idx=graph_1[l].index(k)
                dfs(k,l,idx)
                count+=1

            else:
                break
print(count,end=" ")
count=0
for k in ['G','B']:
    for l in range(len(graph_2)):
        while 1:
            if k in graph_2[l]:
                idx=graph_2[l].index(k)
                dfs2(k,l,idx)
                count+=1
            else:
                break
print(count)