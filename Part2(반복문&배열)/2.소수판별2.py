## template
#문제: n,m이 주어질때 n~m까지 주어지는 모든 소수를 출력하는 프로그램
n,m =map(int,input().split())

if 1<=n<=20000 and 1<=m<=20000:
  for i in range(n,m+1):
    count=0
    for j in range(1,i+1):
      if i%j==0:
        count+=1
    if count==2:
      print(i,end=" ")