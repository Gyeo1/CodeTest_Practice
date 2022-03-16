#https://www.acmicpc.net/problem/1003 실버3 문제

#피보나치 함수? ==> 1,2를 제외하고 이전의 2개의 값들의 합으로 이어지는 함수
#1부터 1 1 2 3 5 8 ... 이렇게 진행된다.
from collections import deque
def fibonacci(fibo,n):
    for _ in range(n-1):
        fibo.append([ fibo[-1][0]+fibo[-2][0], fibo[-1][1]+fibo[-2][1]])
    return fibo


fibo=deque([[1,0],[0,1]])
T=int(input())
check=[]
for _ in range(T):
    check.append(int(input()))
answer=fibonacci(fibo,max(check))
for i in check:
    print(answer[i][0], answer[i][1])