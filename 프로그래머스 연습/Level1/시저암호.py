def solution(s, n):
    answer = ''
    check=0
    for i in s:
        if i == ' ':
            answer=answer+" "
            continue
        else:
            check=ord(i)+n
            #아스키 코드 Z는 z보다 작음 ==>Z를 넘어가려면 소문자 뿐.
            if check>ord("Z") and ord(i)>=ord('A') and ord(i)<=ord("Z"):
                check -= (ord("Z") - ord("A") + 1)
            elif check>ord("z") and ord(i)>=ord('a') and ord(i)<=ord("z"):
                check-=(ord("z")-ord("a")+1)
            answer=answer+chr(check)
    return answer

s="Z Z a z"
n=25
print(solution(s,n))