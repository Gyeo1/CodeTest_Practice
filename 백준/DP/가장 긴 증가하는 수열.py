#https://www.acmicpc.net/problem/11053 실버2

def solution(A):
    check = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if A[i]>A[j]:
                check[i]=max(check[j]+1,check[i])
    print(max(check))


N=int(input())
A=list(map(int,input().split()))

solution(A)

