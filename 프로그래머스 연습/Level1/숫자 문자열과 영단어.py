def solution(s):
    s=list(s) #리스트로 변환.
    check=1
    if len(s)<=50:
        while check:
            for i in range(len(s)):
                if i==len(s)-1:
                    check=0
                    break
                if s[i]=='z':
                    s[i]='0'
                    del s[i+1:i+4]
                    break
                elif s[i]=='o':
                    s[i]='1'
                    del s[i+1:i+3]
                    break
                elif s[i]=='t':
                    if s[i+1]=='w':
                        s[i]='2'
                        del s[i + 1:i + 3]
                        break
                    elif s[i+1]=='h':
                        s[i]='3'
                        del s[i + 1:i + 5]
                        break
                elif s[i]=='f':
                    if s[i+1]=='o':
                        s[i]='4'
                        del s[i+1:i+4]
                        break
                    if s[i+1]=='i':
                        s[i]='5'
                        del s[i+1:i+4]
                        break
                elif s[i]=='s':
                    if s[i+1]=='i':
                        s[i]='6'
                        del s[i + 1:i + 3]
                        break
                    if s[i+1]=='e':
                        s[i]='7'
                        del s[i + 1:i + 5]
                        break
                elif s[i]=='e':
                    s[i] = '8'
                    del s[i + 1:i + 5]
                    break
                elif s[i]=='n':
                    s[i] = '9'
                    del s[i + 1:i + 4]
                    break

    answer =''.join(s)
    answer=int(answer)
    return answer

a=input()
print(solution(a))