## template

global N,R,result
N,R=map(int,input().split())
result=['0' for i in range(R)]

def check_alpha(alpha,result):
  for i in range(len(result)):
    if result[i]==alpha:
      return 0
  return 1
def GetResult(x): #x번째 for문을 돌려랴
  global N,R,result
  if x>=R:
    for i in range(len(result)):
      print(result[i],end="")
    print("")
  else:
    for i in range(N): #N번째 알파벳에서 멈춰
      alpha=chr(ord('a')+i)
      if check_alpha(alpha,result):
        result[x]=alpha
        GetResult(x+1)
        result[x]=0
GetResult(0)