def solution(arrA, arrB):
    arrA_idx = 0
    arrB_idx = 0
    arrA_len = len(arrA)
    arrB_len = len(arrB)
    answer = []
    while arrA_idx < arrA_len and arrB_idx < arrB_len:  # A, B 둘 다 남아있을때 사용하는 while문
        # idx가 len까지 오면 해당 array는 비워진것
        if arrA[arrA_idx] < arrB[arrB_idx]:
            answer.append(arrA[arrA_idx])
            arrA_idx += 1
        else:
            answer.append(arrB[arrB_idx])
            arrB_idx += 1
    while arrA_idx < arrA_len:
        answer.append(arrA[arrA_idx])
        arrA_idx += 1
    while arrB_idx < arrB_len:
        answer.append(arrB[arrB_idx])
        arrB_idx += 1
    return answer
