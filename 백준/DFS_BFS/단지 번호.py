#문제: N*N 평면이 있다, 1이 있는 곳은 집(단지), 0은 빈속이라 하면
# 1이 연결된 단지들의 갯수와 단지를 이루고 있는 집의 갯수를 체크해라
size=int(input())
graph=[]
for i in range(size):
    graph.append(list(map(int,input())))

def dfs(x,y):
    global count
    if x<=-1 or y<=-1 or x>=size or y>=size:
        return
    if graph[x][y]==1:
        graph[x][y]=0 #현재 위치를 0으로 만들고 count를 1 시킴
        #count는 단지의 갯수다.
        # print(count)
        count+=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
number=0
check=[]
for i in range(size):
    for j in range(size):
        if graph[i][j]==1:
            number+=1
            count=0
            (dfs(i,j))
            check.append(count)
print(number)
check.sort()
for i in check:
    print(i)