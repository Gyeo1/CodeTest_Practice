def solution(prices):
    INF = 1000000001
    tmp = INF
    answer = -INF
    for price in prices:
        if tmp != INF:
            # answer = max(answer, tmp - price) 기존 코드이다
            answer = max(answer, price - tmp)  # 고친 부분 tmp는 이전의 주식 값중 최저점 매수한 주식 값이고 price 현재 기준 주식 값이다
            # 당연히 이익을 따질때는 현재 가격 - 최 저점을 따져야 되므로 바꿈

        tmp = min(tmp, price)  # 여기서 제일 주식 가격이 작을때를 넣어둔다.
    return answer


prices1 = [1, 2, 3]
ret1 = solution(prices1)

print("solution 함수의 반환 값은", ret1, "입니다.")

prices2 = [3, 1]
ret2 = solution(prices2)

print("solution 함수의 반환 값은", ret2, "입니다.")
