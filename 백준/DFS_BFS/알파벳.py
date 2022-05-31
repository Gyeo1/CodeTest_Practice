# https://www.acmicpc.net/problem/1987 골드 4 문제

import sys

sys.setrecursionlimit(10 ** 6)
# R,C의 격자로 알파벳들이 정렬됨 이때 말은 0,0에있고 말은 상,하,좌,우로 이동 가능하다
# 말은 움직일때 이전에 건너갔던 알파벳이 있는 곳으로 갈 수 x 즉 하나의 알파벳씩만 밟아서 갈 수 있는 최대 거리?

# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
#
# def dfs(current,check_sum):  # 현재 위치, 현재 지나온 알파벳 정보
#     global max_len
#
#     if max_len == 26 :  # 이거 걸어둬야됨 아니면 시간 초과난다.
#         return
#     max_len=max(max_len,check_sum)
#     for i in range(len(dx)):    # 상 하 좌 우 좌표 확인용
#         next_y = current[1] + dy[i]
#         next_x = current[0] + dx[i]
#         if -1<next_x <C and -1<next_y < R and check[ord(maze[next_y][next_x]) - ord("A")]==0:  # next 좌표가 maze 범위에 있으면?
#             check[ord(maze[next_y][next_x]) - ord("A")]=1
#             dfs([next_x,next_y],check_sum+1)
#             check[ord(maze[next_y][next_x]) - ord("A")]=0

#Pypy로 맞춤 python3는 시간초과가 계속난다 ㅅㅂ..
def dfs(x,y,cnt): #현재 위치, 현재 지나온 알파벳 정보
    global max_len
    max_len=max(max_len,cnt)
    if max_len==26: # 모든 알파벳을 지나왔으면 더이상 진행할 필요가 x
        return
    for i in range(4):
        next_y=y+dy[i]
        next_x=x+dx[i]
        if -1<next_x<C and -1<next_y<R and not maze[next_y][next_x] in check:
            #next 좌표가 maze 범위에 있고 해당 알파벳을 안지나 갔으면?
            check.add(maze[next_y][next_x])  # 현재 위치의 알파벳을 넣어준다
            dfs(next_x,next_y,cnt+1) #아니면 다음 좌표로 이동
            check.remove(maze[next_y][next_x])


R, C = map(int, input().split())  # R은 세로 C는 가로 좌측 상단(0,0)에 말이 놓여있다
max_len = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
maze = []
check = set()   # check는 A-Z까지 사용됐는지 여부를 확인한다
# visited=[[False for _ in range(C)] for _ in range(R)]


for i in range(R):
    char = input()
    maze.append(list(char))  # 문자열을 list로 한글자씩 넣는 방법이다. for문 안써도됨
check.add(maze[0][0])
dfs(0,0,1)
print(max_len)