## template
#문제: n층의 삼격형을 출력하시오.
n= int(input())
if 0<=n<=100:
  for i in range(1,n+1):
    for j in range(i):
      print("*",end='')
    print("")