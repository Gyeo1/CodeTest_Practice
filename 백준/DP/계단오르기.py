# https://www.acmicpc.net/problem/2579      실버 3문제

#계단을 오르는 규칙 1. 계단은 한번에 한계단 or 두 계단씩 오를 수 있다.
#2.연속된 세 개의 계단을 모두 밟아서는 안된다. 단 시작점은 계단 x
#3. 마지막 도착 계단은 반드시 밟아야 한다. ==> 뒤에서 부터 시작해야되나?

n=int(input())
stair=[]
check=[0 for _ in range(n)]
for _ in range(n):
    stair.append(int(input()))
print(stair)
check[0]=stair[0]
check[1]=max(stair[2],check[0]+stair[1])
check[2]=max(stair[0]+stair[2],stair[1]+stair[2]) #처음 계단을 밟고 3번째 계단을 밟은지, 2번째 계단을 밟고 3번째 계단을 밟는디

for i in range(3,n):
    check[i]=max(check[i-2]+stair[i], stair[i]+stair[i-1]+check[i-3])
print(check)