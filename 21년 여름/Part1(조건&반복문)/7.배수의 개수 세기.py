## template
#문제: 자연수 A,B,C가 주어질때 A~B까지 숫자중 C의 배수를 출력하도록.
#A와 B의 숫자 크기에 따라 코드 생각하기.
A,B,C = map(int,input().split())
count=0
D=0
if 1<=A<=1000 and 1<=B<=1000 and 1<=C<=1000:
  if A>B:
    D=A
    A=B
    B=D
  for i in range(A,B+1):
    if i%C==0:
      count+=1
  print(count)