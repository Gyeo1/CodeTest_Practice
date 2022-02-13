# https://www.acmicpc.net/problem/9935     골드4 문제
from collections import deque
import sys
# input=sys.stdin.readline
# def find_burst(string,burst):
#     start = 0
#     idx = string.find(burst, start)
#     if idx==-1:
#         return -1
#     return idx
#
# string=input()
# burst=input()
#
# while 1:
#     del_idx=find_burst(string,burst)
#
#     if del_idx==-1:
#         break
#     string=string[:del_idx]+string[del_idx+len(burst):]
#
# if string:
#     print(string)
# else:
#     print("FRULA")
string=input()
burst=input()
Q=[]
for i in string:
    Q.append(i)
    if len(Q)<len(burst):
        continue
    if "".join(Q[-len(burst):])==burst:
        for j in range(len(burst)):
            Q.pop()
if Q:
    print("".join(Q))
else:
    print("FRULA")