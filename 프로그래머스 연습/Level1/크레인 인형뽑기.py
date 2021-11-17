#NxN 격자가 있고 인형을 뽑는다. 동일한 인형을 뽑는다면 인형이 터져서 사라진다. 터지면 answer에 +2

def solution(board, moves):
    store=[]
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] !=0: #
                store.append(board[j][i-1])
                board[j][i - 1]=0
                break
        if len(store)>=2 and store[len(store)-1]==store[len(store)-2]:
            del store[len(store)-2:]
            answer+=2

    return answer

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
print(solution(board,moves))