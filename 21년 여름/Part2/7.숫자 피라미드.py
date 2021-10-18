## template.
#문제: 숫자를 주어지는 값S부터 N층의 피라미드로 쌓기(9를 넘어가면 1부터 시작) 만약 층이 홀수층이면 반대로 .
N,S= map(int, input().split())
result=[]
if 1<=N<=100 and 1<=S<=9:
  for i in range(1,N+1):
    for j in range(N-i):#이 for문은 공백을 채우기 위함 층이 길어질수록 공백이 없어지기 때문에 N-i로 설정
      print("",end=" ")
    for k in range(1,2*(i-1)+2):#이 for문은 숫자를 넣기위함. 층이 늘어날 수록 숫자개수가 많아짐 1-3-5로 증가하는 수식이다.
      result.append(S)#피라미드에 넣을 숫자들을 리스트에 넣어준다.
      S+=1
      if S==10:
        S=1

    if i%2==0:# 숫자를 리스트에 다 넣었으면 층수에 따라 그대로 넣을지 역순으로 넣을지 결정. list.reverse()는 리스트의 값의 순서를 뒤집.
      for l in range(k):
        print(result[l],end="")
    else:
      result.reverse()
      for l in range(k):
        print(result[l],end="")
    result.clear()#비워주기.
    print("")
