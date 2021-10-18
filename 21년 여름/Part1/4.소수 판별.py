## template
#소수? ==>자기 1과 자기자신 빼고 나눠지는 수가 없는 숫자이다.
n=int(input())
a=0
if 1<=n<=20000:
  for i in range(1,n+1):
    if n%i==0 :
      a+=1
  if a==2:
    print("YES")
  else:
    print("NO")