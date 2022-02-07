#https://www.acmicpc.net/problem/11719 브론즈 1문제
while True:
    try:
        a=input()
        print(a)
    except EOFError: #EOF 에러 ==> end of file의 약자로(Ctrl+d가 실행될때 나옴?) EOF
        break