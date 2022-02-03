#https://www.acmicpc.net/problem/10845      실버 4문제

import sys
input=sys.stdin.readline
command_num=int(input())
queue=[]
for _ in range(command_num):
    command=input().split() # 공백 기준으로 split 한다.
    if command[0]=='push':
        queue.append(command[1])
    elif command[0]=='pop':
        if queue:
            print(queue[0])
            del queue[0]
            continue
        print(-1)
    elif command[0]=='size':
        print(len(queue))

    elif command[0]=='empty':
        if queue:
            print(0)
            continue
        print(1)

    elif command[0]=='front':
        if queue:
            print(queue[0])
            continue
        print(-1)

    else: #back 명령어 -->큐의 가장 뒤에 있는 정수.
        if queue:
            print(queue[-1])
            continue
        print(-1)