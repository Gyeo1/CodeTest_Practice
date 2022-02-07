#https://www.acmicpc.net/problem/4949 실버4문제
from collections import deque
def find_equal(s):
    for i in s:
        if i == "(":
            Q.append(i)
        elif i == "[":
            Q.append(i)

        elif i == ")":
            if len(Q) == 0:  # 만약 큐가 비어 있다. 즉 )로 시작되면 에러
                print("no")
                return
            if Q[-1] == "(":
                Q.pop()  # 만약 마지막 괄호가 (면 pop
            elif Q[-1] == "[":
                print("no")
                return
        elif i == "]":
            if len(Q) == 0:
                print("no")
                return
            if Q[-1] == "[":
                Q.pop()
            elif Q[-1] == "(":
                print("no")
                return
    if Q:
        print("no")
        return
    print("yes")
while True:
    Q=deque()
    string=input()
    if string !=".":
       find_equal(string)
    else:
        break