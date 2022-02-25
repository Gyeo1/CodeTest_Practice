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
graph_1=[[] for _ in range(N)] #일반인용 그래프
graph_2=[[] for _ in range(N)] #적녹색약 그래프
for i in range(N):
    a=input()
    for j in a:
        graph_1[i].append(j) #일반인은 그냥 정보를 그대로 넣어줌
        if j=="R":
            graph_2[i].append("G")  #적녹 색약은 R/G의 구분을 못하니 R을 G로 바꿔서 저장장
            continue
        graph_2[i].append(j)


count=0
#아래 for문은 일반인의 경우의 수를 구하는 과정
for k in ['R','G','B']:     #일반인은 RGB를 볼 수 있기 때문에 R,G,B를 넣어서 확인
    for l in range(len(graph_1)):
        while 1: #in과 index문을 활용하기 위함 in에 k(color)가 없으면 탈출
            if k in graph_1[l]:
                idx=graph_1[l].index(k)
                dfs(k,l,idx)            #결국 graph의 l번째 줄에 R,G,B를 찾아서 지워주는것
                count+=1
            else:
                break


print(count,end=" ")
count=0
for k in ['G','B']:         #적녹 색맹들은 R,G중 구분을 x, 나는 R을 G로 바꿨기 때문에 G,B만 확인
    for l in range(len(graph_2)):
        while 1:
            if k in graph_2[l]:
                idx=graph_2[l].index(k)
                dfs2(k,l,idx)
                count+=1
            else:
                break
print(count)