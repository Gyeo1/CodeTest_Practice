import sys
Test_num=int(input())
check=[]
sys.setrecursionlimit(10**6)
for case in range(Test_num):
    M,N,K=map(int,input().split())

    graph=[[0 for x in range(M)] for i in range(N)]
    for i in range(K):
        row,col=map(int,input().split())
        graph[col][row]=1

    # for j in range(len(graph)):
    #     print(graph[j])

    def bfs(y,x):
        if x<=-1 or y<=-1 or x>=M or y>=N:
            return
        if graph[y][x]==1:
            graph[y][x]=0
            bfs(y+1,x)
            bfs(y-1, x)
            bfs(y, x+1)
            bfs(y, x-1)

    count=0
    for i in range(N):
        for j in range(M):
            if graph[i][j] ==1:
                count+=1
                bfs(i,j)
    check.append(count)
for i in check:
    print(i)