#https://www.acmicpc.net/problem/10828 실버4 문제
import sys,re
command_num=int(input())
stack=[]
for _ in range(command_num):
    command=sys.stdin.readline().rstrip()
    if "push" in command: # Push임 "push 숫자" 형식이라 push만 확인
        # check=command.split(" ") #split으로 하는게 일반적임
        check= re.findall(r'[0-9]+',command)    #정규 표현식으로 숫자만 긁어오기도 가능

        stack.append(check[0])
    elif command=="pop":
        if stack:
            print(stack[-1])
            del stack[-1]
            continue
        print(-1)
    elif command=="top":
        if stack:
            print(stack[-1])
            continue
        print(-1)
    elif command=="size":
        print(len(stack))
    else:#Empty임
        if len(stack)==0:
            print(1)
            continue
        print(0)