## template
#문제 : N,M 입력받고 N~M까지 출력. 이때 한줄엔 8개 숫자만 쓸것.
N,M=map(int,input().split())
count=0
if N<=M<=1000:
  for i in range(M-N+1):
    print(N+i,end=" ")
    count+=1
    if count==8:
      print("")
      count=0