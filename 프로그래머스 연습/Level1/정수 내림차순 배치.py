def solution(n):
    answer = 0
    n = str(n)
    n = sorted(n, reverse=True)
    answer = int(''.join(n))
    return answer
#다음처럼 한줄로 정리도 가능하다.
# answer=int(''.join((sorted(str(n),reverse=True))))
a=1000020
print(solution(a))
