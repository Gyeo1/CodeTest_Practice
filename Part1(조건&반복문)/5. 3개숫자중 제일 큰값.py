## template
a,b,c= map(int,input().split())
if 0<=a<=10000 and 0<=b<=10000 and 0<=c<=10000:
  if a>=b and a>=c :
    print(a)
  elif b>=a and b>=c:
    print(b)
  elif c>=a and c>=b:
    print(c)