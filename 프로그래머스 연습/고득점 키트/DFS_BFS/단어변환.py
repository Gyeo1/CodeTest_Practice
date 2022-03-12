#https://programmers.co.kr/learn/courses/30/lessons/43163 레벨3

#Question ==> 두개의 단어와begin target과 단어의 집합 words가 있다
#begin-->target으로 가는 짧은 변환을 words에 있는 단어를 사용해 바꿔라. 단 단어는 한번에 한개씩만 변환 가능하다.
import copy
def dfs(check_word,process,words,target):
    global flag,min_val
    if check_word==target:
        print(check_word, words, process)
        flag=True
        if min_val > process:
            min_val=process
        return
    if words==[]:
        return
    if process> min_val:
        return

    for i in range(len(words)):
        for j in range(len(check_word)): #틀렸던 이유 ==> 3글자 문자만 주어진줄 알았다. 최대 글자는 10글자임!
            next_words = copy.deepcopy(words)
            if check_word[j:j+1] != words[i][j:j+1] and check_word[:j]+check_word[j+1:]==words[i][:j]+words[i][j+1:]:

                next_word=words[i]
                del next_words[i]
                dfs(next_word, process + 1, next_words, target)
    return



def solution(begin, target, words):
    global flag,min_val
    min_val=10**6
    flag=False
    answer = 0
    if target not in words:
        return 0
    # print()

    dfs(begin,0,words,target)
    if flag == True:
        answer=min_val
    return answer

begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]
# begin = "hit"
# target = "hhh"
# words = ["hhh","hht"]
# begin="hit"
# target="cog"
# words=["hot", "dot", "dog", "lot", "log"]
print(solution(begin,target,words))
# if check_word[0]!=words[i][0] and check_word[1]==words[i][1] and check_word[2]==words[i][2]:
#     next_word=words[i][0]+next_word[1:]
#     del next_words[i]
#     dfs(next_word,process+1,next_words,target)
#
# next_word = copy.deepcopy(check_word)
# next_words = copy.deepcopy(words)
# if check_word[1]!=words[i][1] and check_word[0]==words[i][0] and check_word[2]==words[i][2]:
#     next_word= next_word[:1]+words[i][1]+next_word[2:]
#     del next_words[i]
#     dfs(next_word, process + 1, next_words,target)
#
# next_word = copy.deepcopy(check_word)
# next_words = copy.deepcopy(words)
# if check_word[2]!=words[i][2] and check_word[1]==words[i][1] and check_word[0]==words[i][0]:
#     next_word= next_word[:2]+words[i][2]
#     del next_words[i]
#     dfs(next_word, process + 1, next_words,target)