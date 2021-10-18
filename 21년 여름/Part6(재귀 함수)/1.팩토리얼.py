## template
N=int(input())
result=0
def Factorial(N):
  if N==0:
    return 1
  else:
    return N *Factorial(N-1)
print(Factorial(N))