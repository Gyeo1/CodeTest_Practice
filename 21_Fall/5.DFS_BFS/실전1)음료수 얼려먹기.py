N,M =map(int,input().split())
ice=[]
for i in range(N):
    ice.append(list(map(int,input())))
count=0
def dfs(x,y):

    if x<0 or x>=N or y<0 or y>=M:# 만약 인덱스를 벗어난다면 False를 return
        return False

    if ice[x][y]==0:
        ice[x][y]=1 #현재 있는 타일을 1로 채움
        #상하 좌우 모든 면에서 dfs를 다시 실행
        #이렇게 되면 현재 타일과 인접한 모든 타일을 1로 만들어 주면서 하나로 판정을 짓는다.
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False


for i in range(N):
    for j in range(M):
        if dfs(i,j)==True:
            count+=1
print(count)