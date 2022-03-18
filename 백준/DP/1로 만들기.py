#https://www.acmicpc.net/problem/1463 실버 3

#Question==> 정수 X가 주어짐 X가 3으로 나눠 떨어지면 3으로 나눈다. X가 2로 나눠떨어지면 2로 나눈다, 1을 뺀다

# print(10**6)
input_val=int(input())

check=[0]*(input_val+1)

for i in range(2,input_val+1):
    check[i]=check[i-1]+1
    if i%3 ==0:
        check[i]=min(check[i],check[i//3] +1 )
    if i%2==0:
        check[i]=min(check[i],check[i//2]+1)
# print(check)
print(check[input_val])
