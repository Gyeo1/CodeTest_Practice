## template
A=input()
B=input()
count=0
if len(A)<=1000 and len(B)<=1000:
  for i in range((len(A)-len(B))+1):
    for j in range(len(B)):
      if A[i+j]==B[j]:
        count+=1
      else:
        break
    if count==len(B):
      print("YES")
      break
    else:
      count=0
  if count<len(B):
    print("NO")