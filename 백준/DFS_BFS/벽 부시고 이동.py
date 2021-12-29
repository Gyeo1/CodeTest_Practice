from collections import deque
row,col=map(int,input().split()) #N*M의 미로
maze=[]
visited=[]
for _ in range(row):
    maze.append(list(int(x) for x in input()))
visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]
#visited는 벽을 뚫고 지나갔을때랑 안 지나갔을때를 구분짓기 위함[][][여기가 구분하는 지점임!]
# print(maze)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y,crash_check,visited,maze):
    queue=deque()
    queue.append([x,y,crash_check])
    visited[x][y][crash_check]=1 #이게 뭐냐 맨~처음의 check 값을 1로 둔다는 거다.
    while queue:
        x,y,crash_check=queue.popleft()
        if x==row-1 and y==col-1:
            return visited[x][y][crash_check]
        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if next_x <= -1 or next_x >= row or next_y <= -1 or next_y >= col:
                continue
            if maze[next_x][next_y] ==0 and visited[next_x][next_y][crash_check]==0:
                queue.append([next_x,next_y,crash_check])
                visited[next_x][next_y][crash_check]=visited[x][y][crash_check]+1

            if maze[next_x][next_y]==1 and crash_check==0: #만약 벽인데 내가 아직 crash=0 즉 벽을 안깻으면?
                queue.append([next_x,next_y,crash_check+1]) #값을 넣어주는데 크래시값은 +1시켜줘서 0을 벗어나게한다
                visited[next_x][next_y][crash_check+1] = visited[x][y][crash_check] + 1


                #이거는 이제 다음 이동할 칸이 0이고 벽을 안부신 상태를 뜻한다.
    return -1

print(bfs(0,0,0,visited,maze))