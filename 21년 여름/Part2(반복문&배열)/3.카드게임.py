## template
#문제: A,B가 내는 카드를 입력하고 숫자가 높은 카드를 더 많이 낸 사람이 승리
A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]
count1=0 #누가 이겼을때 카운트 값 올리고 내리는지?
for i in range(10):
  if A[i] >B[i]:
    count1+=1
  elif A[i]<B[i]:
    count1-=1
if count1>0:
  print("A")
elif count1<0:
  print("B")
else:
  print("D") #비겼을때 D