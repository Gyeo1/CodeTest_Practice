# https://www.acmicpc.net/problem/9095 실버3

#Question: 정수4를 1,2,3의 합으로 나타내는 방법은 7가지가 있다. 합을 나타낼때는 하나 이상의 수로 표현해라

#문제에서 1, 2, 3까지는 쉽게 구한다 1은 1가지 2는 2가지 3은 4가지의 방법이있다.
#여기서 1,2,3으로만 이뤄져 있는게 핵심이다.
#4에서 1을 빼면 3이남은 3을 만들수 있는 방법은 4가지임 , 2를 빼면 2가남고 2를 만드는 방법은 2가지이다
#마지막으로 3을 빼면 1이 남는데 1을 만드는 방법은 1가지이므로 4+2+1 =7이다
#마찬가지로 5를 만드는 방법은 4를 만드는 가짓수(7)+ 3을만드는 가짓수(4)+ 2를만드는 가짓수(2) 13임


check=[0 for _ in range(11)]
check[1]=1
check[2]=2
check[3]=4
for i in range(4,11):
    check[i]=check[i-1]+check[i-2]+check[i-3]
n=int(input())
for _ in range(n):
    print(check[int(input())])

