## template
global n,result,previous
n=int(input())
result=[]
previous=[]

def mountain(n,step):
  global result, previous
  if step>n:
    print(''.join(map(str,result)))
  else:
    result.append(step) #이전 값을 저장할 것은?
    if step==1:
      previous.append(1)
    else:
      result=result+previous
      previous=result
    if step>2:
      del previous[len(previous)-1]
    mountain(n,step+1)
if 1<=n<20:
  mountain(n,1)