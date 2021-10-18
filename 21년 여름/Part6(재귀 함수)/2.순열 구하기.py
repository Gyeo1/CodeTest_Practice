global N,R
N,R= map(int,input().split())
result=[0 for i in range(R)]
#N은 알파벳의 개수 R은 for문의 갯수?
check=[False for i in range(N)]
def permute(x,result):
  global N,R
  if x>=R:
      # 쉼표로 구분하여 문자열로 결합하기 !
      #s = ",".join(lst)
    s="".join(result)
    print(s)
  else:
    for i in range(N): #N인 이유? 알파벳은 N까지 있기 때문.
      alpha=chr(ord('a')+i)
      if check[i]==False:
        result[x]=alpha
        check[i]=True
        permute(x+1,result)
        check[i]=False
        result[x]='0'
if 1<=N<=10 and 0<=R<=min(N,7):
  permute(0,result)