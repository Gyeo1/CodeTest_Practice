def solution(N, votes):
    vote_counter = [0 for i in range(N + 1)]
    for i in votes:
        vote_counter[i] += 1

    max_val = max(vote_counter)

    answer = []
    for idx in range(1, N + 1):
        if vote_counter[idx] == max_val:
            answer.append(idx)#수정 한 부분! 원래는 answer.append(vote_counter[idx])였음
            #vote_counter[idx]는 몇표를 받았는지의 값이므로 idx를 넣어야됨
    return answer
