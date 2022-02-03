#로그의 앞부분은 식별자, 문자로 구성된 로그가 숫자로그보다 앞에온다
#식별자는 순서에 영향을 안주지만 ,문자가 동일하면 식별자 순으로! 숫자 로그는 입력 순서대로
log=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
digit_log=[]
string_log=[]
for i in log:
    if i.split()[1].isdigit()==True: #로그의 첫번째가 숫자면 숫자로그.
        digit_log.append(i)
    else:
        string_log.append(i)
string_log.sort(key= lambda x: (x.split()[1],x.split()[0]))
#람다에서 key를 사용해 정렬 방법을 정의 할 수 있다. x를 받으면 x.split을해 1 인덱스의 값을 비교하던가 0의 값을 비교!

print('숫자 로그: ',digit_log)
print('문자열 로그: ',string_log)
string_log.extend(digit_log)
print(string_log)
#숫자로그는 순서대로 정렬이니 그냥 출력하면됨
