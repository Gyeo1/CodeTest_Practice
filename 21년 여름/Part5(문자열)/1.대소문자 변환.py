## templat
#chr()는 아스키 코드(int)를 문자로 바꾸고
#ord는 문자를 아스키 코드(int)로 바꿔준다.
str1=input()
if 0<=len(str1)<=1000:
  for i in range(len(str1)):
    count=0
    if 65<=ord(str1[i])<=90:
      count=ord(str1[i])+32
      print(chr(count),end="")
    elif 97<=ord(str1[i])<=122:
      count=ord(str1[i])-32
      print(chr(count),end="")
    else:
      print(str1[i],end="")