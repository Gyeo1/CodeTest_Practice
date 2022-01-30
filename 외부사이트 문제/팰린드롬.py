#팰린드롬 알고리즘? ==> 문자열의 앞뒤를 뒤집어도 같은 문자인지 판별하는 알고리즘, 대소문자 상관x
#
import re
problem="A man, a plan, a canal: Panama"

def Plaindrome(s):
    s=s.lower()             #소문자로 만들고
    s=re.sub(r'[^0-9a-z]',"",s)
    #sub 함수는 [패턴문자][바꿀 문자] [적용시킬 대상]의 형태로 패턴의 문자를 바꿀 문자로 바꿔준다.
    return s==s[::-1]       #뒤집은 거랑 그냥 s랑 bool 형태로 return
check=Plaindrome(problem)
print(check)