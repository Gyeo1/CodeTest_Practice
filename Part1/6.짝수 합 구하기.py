## template
#문제: 1~N까지 숫자중 짝수의 합을 구하기.
N=int(input())
result=0
if 1<=N<=2000:
  for i in range(1,N+1):
    if i%2==0:
      result+=i
  print(result)