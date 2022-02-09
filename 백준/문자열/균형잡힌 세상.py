#https://www.acmicpc.net/problem/4949 실버4문제
from collections import deque
def find_equal(s):
    for i in s:
        #if 문 4줄은 [, (일시 무조건 넣는다는 의미이다.
        if i == "(":
            Q.append(i)
        elif i == "[":
            Q.append(i)

        #아래 부터는 ), ]일시 조건에 따라 pop시킬지 NO할지 판단하는 문
        elif i == ")":
            if len(Q) == 0:  # 만약 큐가 비어 있다. 즉 )로 시작되면 에러
                print("no")
                return
            if Q[-1] == "(":
                Q.pop()  # 만약 마지막 괄호가 (면 pop 즉()가 완성이 되면 (를 내보낸다
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