# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def func_a(numA, numB, exp):
    if exp == '+':
        return numA + numB
    elif exp == '-':
        return numA - numB
    elif exp == '*':
        return numA * numB


def func_b(exp):
    print(list(enumerate(exp)))  # enumerate는 문자열/리스트의 원소에 숫서 값(index)를 부여하는 함수로 enumerate 객체를 return함
    # enumerate는 객체를 반환해서 값을 확인하려면 list형태로 변환해서 확인해라
    for index, value in enumerate(exp):
        if value == '+' or value == '-' or value == '*':
            return index


def func_c(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx + 1:])
    return numA, numB


####
def solution(expression):
    exp_index = func_b(expression)  # 첫번째 빈칸: func_b는 문자열에서 기호의 위치 index를 찾기위한 함수임 enumerate가 핵심이다.

    first_num, second_num = func_c(expression, exp_index)  # 두 번째 빈칸으로 기호 index 기준으로 앞, 뒤 숫자를 찾는 함수

    result = func_a(first_num, second_num, expression[exp_index])  # 세 번째 빈칸: 함수, 기호값으로 값을 도출하는 함수 3번째 인자가 핵심이다.
    # func_a의 3번째 인자는 +,- 같은 기호를 보내야되는데 exp_index는 index가 있는거지 기호가 있는게 아니므로
    # 해당 기호를 보내기 위해서는 expression[index]방식으로 문자열에서 기호를 찾아서 보내야된다.

    return result


###
expression = "123+12"
ret = solution(expression)

print("solution 함수의 반환 값은", ret, "입니다.")
