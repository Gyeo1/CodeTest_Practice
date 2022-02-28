#https://programmers.co.kr/learn/courses/30/lessons/42577 level2?

#Question: 전화번호 부에 적힌 전화번호중 한 번호가 다른 번호의 접두어인 경우 찾기

#2)

def solution(phone_book):
    check=dict()
    phone_book.sort(key=lambda x: len(x)) #1)phone_book을 길이 순서대로 정렬
    prefix_len=len(phone_book[0])         #제일 짧은 길이 저장
    long_len=0
    answer=True

    for i in phone_book:
        if len(i)>prefix_len:             #2)현재 phone number가 최소 길이보다 길다?
            long_len=len(i)               # long_len에 길이 저장


        if long_len!=0:                 #3) long_len이 0이 아니다 즉 최소 전화번호 길이보다 긴 값을 발견했다?
            for j in range(prefix_len,long_len+1):      #제일 짧은 길이부터~ 긴 길이까지 phone number를 잘라서 확인
                if i[:j] in check.keys():               #만약 check에 해당 범위의 값이 있다? 그럼 prefix가 겹치는거임
                    return False
            check[i]=0                                  #check에 해당 값이 없으면 prefix를 dict자료형으로 추가해줌

        else:                            #4) long_len이 0이면 아직 전화번호의 길이가 최소 prefix와 같음
            if i[:prefix_len] not in check.keys():  #간단하게 phonenumber[:prefix길이]까지 검증을 거치면된다.
                check[i]=0
            else:
                answer=False

    return answer

phone_book=["97674223","119", "1195524421"]
# phone_book=["123","456","789"]
# phone_book=["12","123","1235","567","88"]
# phone_book=["934793", "34", "44", "9347"] #중요한 반례임
print(solution(phone_book))