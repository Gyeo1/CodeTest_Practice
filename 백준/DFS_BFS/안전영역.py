#https://www.acmicpc.net/problem/2468  실버1문제

#문제: 높이 정보가 주어졌을때 안전 영역의 최대 개수를 계산하는 프로그램 작성
# def dfs2()
import copy,sys
sys.setrecursionlimit(10**6)
def dfs(y,x):
    global check_maze
    check_maze[y][x]=0

    # if x+1>N or y+1>N or x-1<0 or y-1<0:
    #     return
    # else:
    if x+1<N and check_maze[y][x+1]!=0:
        dfs(y,x+1)
    if x-1>=0 and check_maze[y][x-1]!=0:
        dfs(y,x-1)
    if y+1<N and check_maze[y+1][x]!=0:
        dfs(y+1,x)
    if y-1>=0 and check_maze[y-1][x] !=0:
        dfs(y-1,x)
    # else:
    #     return
    # # return


answer=1 #안잠길수 있으니 1로
N=int(input())
graph=[]
max_hegith=0
min_hegith=100
for i in range(N):
    a=map(int,input().split())
    graph.append(list(a))
    check_1=max(graph[i])
    check_2=min(graph[i])
    if max_hegith<check_1:
        max_hegith=check_1
    if min_hegith>check_2:
        min_hegith=check_2

for j in range(min_hegith,max_hegith+1):
    for k in range(len(graph)):         #물에 잠긴 지역을 0으로 바꾼다
        while 1:
            if j in graph[k]:
                idx=graph[k].index(j)
                graph[k][idx]=0
            else:
                break
    # print(graph)
    check_maze=copy.deepcopy(graph)
    # print(check_maze)
    number=0
    for l in range(len(check_maze)):
        for m in range(len(check_maze[l])):
            if check_maze[l][m]!=0:   #시작점
                dfs(l,m)
                # print(check_maze)
                number+=1
    answer=max(number,answer)
print(answer)