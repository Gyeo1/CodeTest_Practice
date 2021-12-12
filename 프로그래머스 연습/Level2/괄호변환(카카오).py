def solution(p):
    answer = ''
    u="" #u는 반드시 균형, v는 빈 문자열 가능
    v=""
    count=0
    trigger=0
    for i in range(len(p)):#u,v 나누기.
        if p[i]=="(":
            count+=1
            if len(v)==0:
                v += p[i]
                trigger = 1
                continue
        else:
            count-=1
            if len(v) == 0:
                v += p[i]
                trigger = -1
                continue
        v += p[i]
        if count==0 and trigger==1:
            trigger=0
            u+=v
            v=""
    print(u)
    print(v)
    return answer


p="()))((()"
print(solution(p))
#균형잡힌 괄호 문자열 p 가 주어지면  올바른 괄호 문자열(괄호가 짝도 맞을때)로 리턴하세요
#균형 잡힌? ==> )(의 갯수가 같을때
#올바른? ==> ()의 짝도 맞을때.
'''
<문제에서 제공하는 풀이 과정>
1.입력이 빈 문자열이면 빈거 반환
2.문자열 w를 균형잡힌 문자열 u,v로 분리 u는 균형잡힌 문자열로 더이상 분리 x, v는 빈 문자열 가능
3.문자열 u가 올바른 괄호 문자열이면 v에 대해 1단계 부터 실행 (==>재귀?) 해당 결과를 u에 붙여준다.
4.문자열 u가 올바른 괄호 문자열이 아니면 아래 과정을 수행
    4-1. 빈 문자열에 첫번째 문자로 ( 붙이기
    4-2. 문자열 v에 대해 1단계 부터 재귀적으로 수행한 결과를 이어 붙임
    4-3. )를 다시 붙인다
    4-4. u의 첫번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다
    4-5. 생성된 문자열을 반환.
    
'''