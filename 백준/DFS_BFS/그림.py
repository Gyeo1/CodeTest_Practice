import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    global area
    maps[y][x] = 0  # 1 인 부분을 0으로 만들기
    #벡터 쓰지 않고 노가다로 실행
    # for i in range(4):  # 4방향중 1인 부분 찾기
    #     next_x = x + dx[i]
    #     next_y = y + dy[i]
    #     if -1 < next_y < n and -1 < next_x < m and maps[next_y][next_x] == 1:
    #         area += 1
    #         dfs(next_x, next_y)
    if -1<y-1<n and maps[y-1][x]==1:
        area+=1
        dfs(x,y-1)
    if -1<y+1<n and maps[y+1][x]==1:
        area+=1
        dfs(x,y+1)
    if -1<x-1<m and maps[y][x-1]==1:
        area+=1
        dfs(x-1,y)
    if -1<x+1<m and maps[y][x+1]==1:
        area+=1
        dfs(x+1,y)


def solution():
    global area
    answer = 0
    answer_area = 0  # 그림이 없을 경우를 대비해 0을 넣어둔다
    for i in range(n):
        while 1 in maps[i]:  # 1인 부분(그림 part)를 찾는다
            area = 1
            answer += 1
            idx = maps[i].index(1)
            dfs(idx, i)
            answer_area=max(area,answer_area) # 틀렸던 부분 list를 만들고 append 했는데 그러면 메모리 초과가 뜬다.
    print(answer)
    print(answer_area)
n, m = map(int, input().split())  # n은 세로 m은 가로이다.
maps = []
# 방향 벡터 때문에 메모리 초과가 발생한듯
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
for _ in range(n):
    maps.append(list(map(int, input().split())))

solution()
