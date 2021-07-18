## template
document=input()
check=[]
if len(document)<100000:
  for i in range(len(document)):
    if ord(document[i])!=32:#32는 아스키 코드로 공백을 의미 한다.
      print(document[i],end="")