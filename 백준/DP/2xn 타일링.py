#https://www.acmicpc.net/problem/11726 실버3 문제

#Q) 2*n 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하세요



n=int(input())
check=[0 for _ in range(1001)]
check[1]=1
check[2]=2

for i in range(3,n+1):
    check[i]=check[i-1]+check[i-2]
print(check[n]%10007)
#문제의 핵심! n=1,2일경우는 고정이다
#핵심은 n=3부터인데 제일 왼쪽 기준으로 2*1 타일을 넣으면 오른쪽에는 2칸이 남고 그것은 n=2일때의 값과 같다
#반대로 1*2 타일을 넣으면 오른쪽에는 1칸이 남고 그것은 n=1인 경우와 같다
#즉 check[n]=check[n-1] + check[n-2]라는 식이 완성됨
