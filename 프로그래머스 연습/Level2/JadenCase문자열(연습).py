def solution(s):
    s=s.split(' ')  #문제의 핵심이다 result에서 띄어쓰기까지 다시 받아와야 되기 때문에 split을 " "을 기준으로 해줘야된다.
    print(s)
    for i in range(len(s)):
        if s[i]=="":
            continue
        first_val=ord(s[i][0])
        if (first_val>=ord('a') and first_val<=ord('z')) :
            first_val-=32
            s[i]=chr(first_val)+s[i][1:]
        for j in range(1,len(s[i])):
            next_val=ord(s[i][j])
            if (next_val >= ord('A') and next_val <= ord('Z')):
                next_val += 32
            s[i]=s[i][:j]+chr(next_val)+s[i][j+1:]
    answer=" ".join(s)
    return answer


s=" 3 aaaaa aaa          asd"
print(solution(s))