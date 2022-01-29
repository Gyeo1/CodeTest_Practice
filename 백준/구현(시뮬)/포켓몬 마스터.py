#https://www.acmicpc.net/problem/1620 실버4

import sys
# input=sys.stdin.readline

pocket_number, problem= map(int, sys.stdin.readline().split())
dictonary=dict()
number=1
for i in range(1,pocket_number+1):
    name=sys.stdin.readline().rstrip()
    dictonary[name]=str(i)
    dictonary[str(i)]=name
list_value=list(dictonary.values())
# print(dictonary)
# print(list_value)
# print(list_key,type(list_key[1]))
for _ in range(problem):
    check=sys.stdin.readline().rstrip()
    print(dictonary[check])
# for i in range(problem):
#     check=sys.stdin.readline().rstrip()
#     if check in list_value: #포켓몬의 이름을 받는다면
#         print(list_value.index(check)+1) #인덱스 값은 0부터 시작하니깐 +1 해준다
#         continue
#     print(dictonary[int(check)])
#     # print(list_value.index(check))                  #만약 문제가 포켓몬 이름을 물어보면
