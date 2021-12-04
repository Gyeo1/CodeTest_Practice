def solution(s):
    answer = ''
    int_list = []
    check = ""
    for i in range(len(s)):
        if s[i] != " ":
            check+=s[i]
            if i<len(s)-1:
                continue
        int_list.append(int(check))
        check=""

    print(int_list)
    answer +=str(min(int_list))
    answer +=" "
    answer += str(max(int_list))
    return answer

s="-1 -2 -3 -4 11 12 12"

print(solution(s))
#아 11이나 111도 생각해라! 공백 전까지의 문자를 append 해라