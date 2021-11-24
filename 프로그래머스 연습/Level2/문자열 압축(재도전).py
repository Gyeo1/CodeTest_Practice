def solution(s):
    answer = len(s)
    for i in range(len(s)):
        check=s[:i+1]     #확인할 리스트
        count=1
        s_new=""
        for j in range(i+1,len(s),i+1):
            if len(s_new)>answer:
                break
            if check==s[j:j+1+i]: #이후에 나오는 문자가 겹치면? ==> j+1+i는 수식이다
                count+=1
            else: #안겹치면 종료
                if count!=1:
                    s_new+=str(count)
                #아래 3줄이 핵심. check의 값을 바꾸고 그 뒤를 확인하는 것이다.
                s_new+=check
                check=s[j:j+1+i]
                count=1

        if count != 1:
            s_new += str(count)
        s_new += check

        if len(s_new)<answer:
            answer=len(s_new)
    return answer

s="ababcdcdababcdcd"
print(len(s))
a=solution(s)
print(a)