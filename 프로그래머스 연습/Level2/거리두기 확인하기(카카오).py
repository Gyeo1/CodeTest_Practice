def solution(places):
    target_P = 'P'
    target_X = "X"
    answer = [1, 1, 1, 1, 1]
    for i in range(len(places)):
        trigger=1
        check = [[0 for a in range(5)] for b in range(5)]  # 빈 리스트 생성

        for j in range(len(places[i])):
            index_P = -1
            index_X = -1
            print(places[i][j])
            while True:
                index_P = places[i][j].find(target_P, index_P + 1)
                if index_P == -1:
                    break
                check[j][index_P] -=1
                if j>0:#하
                    check[j-1][index_P]-=1
                if j<4:
                    check[j+1][index_P] -=1
                if index_P>0:
                    check[j][index_P-1] -=1
                if index_P<4:
                    check[j][index_P+1] -=1

            while True:  # X의 좌표를 찾는다.
                index_X = places[i][j].find(target_X, index_X + 1)
                if index_X == -1:
                    break
                check[j][index_X] += 5

        print(check)
        for l in range(len(check)):
            for k in  range(len(check[l])):
                if check[l][k]<=-2:
                    answer[i]=0
                    trigger=0
                    break
            if trigger==0:
                break
    return answer

palces=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
       ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PPPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(palces))

#문제 접근 방식,0이들어있는 5*5 배열을 만들고 P와 X가 들어가는 인덱스를 찾은 뒤
#P의 인덱스의 상하좌우엔 -1을 더해주고 X의 인덱스에는 5를 더해준다