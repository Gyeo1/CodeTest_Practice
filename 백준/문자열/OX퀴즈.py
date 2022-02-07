#https://www.acmicpc.net/problem/8958 브론즈2 문제
number=int(input())
for _ in range(number):
    answer=0
    trig=1
    string=input()
    for i in string:
        if i=="O":
          answer+=trig
          trig+=1
          continue
        else:
            trig=1
    print(answer)