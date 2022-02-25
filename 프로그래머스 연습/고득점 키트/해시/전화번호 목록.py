#https://programmers.co.kr/learn/courses/30/lessons/42577 level2?

#Question: 전화번호 부에 적힌 전화번호중 한 번호가 다른 번호의 접두어인 경우 찾기

def solution(phone_book):
    check=dict()
    phone_book.sort(key=lambda x: len(x))
    prefix_len=len(phone_book[0])
    long_len=0

    # print(prefix[:prefix_len])
    answer=True
    # for i in range(1,len(phone_book)):
    #     if phone_book[i][:prefix_len]==prefix:
    #         answer = 'false'
    #         break
    for i in phone_book:
        # print(check)
        if len(i)>prefix_len:
            long_len=len(i)
        if long_len!=0:
            for j in range(prefix_len,long_len+1):
                if i[:j] in check.keys():
                    return False
            check[i]=0
        else:
            if i[:prefix_len] not in check.keys():
                check[i]=0
            else:
                answer=False

    return answer

phone_book=["97674223","119", "1195524421"]
# phone_book=["123","456","789"]
# phone_book=["12","123","1235","567","88"]
# phone_book=["934793", "34", "44", "9347"]
print(solution(phone_book))