def solution(new_id):
    new_id=list(new_id) #리스트로 변환
    if len(new_id)>=1 and len(new_id)<=1000:
        check=[]
        #Step1 대문자 소문자로 바꿔주기
        for i in range(len(new_id)):
            a=ord(new_id[i])
            if a>=65 and a<=90:
                a+=32
                new_id[i]=chr(a)
        #Step2 알파벳 소문자 숫자 - _ . 제외하고 모두 제거
        for j in range(len(new_id)):
            a = ord(new_id[j])
            if (a>=97 and a<=122) or (a>=48 and a<=57) or a==45 or a==95 or a==46:
                continue
            else:
                check.append(new_id[j])
        for k in check:
            new_id.remove(k)
        #Step3. 마침표(.)이 연속되어서 나오면(두번이상)하나의 마침표로 바꿔준다.

        while 1:
            count=0
            for l in range(len(new_id)):
                if l+1<len(new_id) and new_id[l]==new_id[l+1]=='.' :
                    del new_id[l]
                    break
                else:
                    count+=1
            if count==len(new_id):
                break

    #원래하던게 왜 안됐을까? ==>for 문으로 del을 할시 지워지고 나서의 인덱스기준으로 다시 지우기 때문이다.


        #Step4 마침표가 처음이나 끝에있으면 지워라.
        if new_id[0]=='.':
            del new_id[0]
        if len(new_id)>0 and new_id[len(new_id)-1]=='.':
            del new_id[len(new_id)-1]
        #Step5  문자열이면 a를 넣는다
        if len(new_id)==0:
            new_id.append('a')
        #Step6 16자 이상이면 15이후 문자들을 다 지워라. 지우고 맨 뒤가 .이면 .도 지워라
        if len(new_id)>15:
            del new_id[15:len(new_id)]
            if new_id[len(new_id)-1]=='.':
                del new_id[len(new_id)-1]

        #Step7 new_id의 길이가 2자 이하면 마지막 문자를 길이가 3될때까지 복사
        while len(new_id)<3:
            new_id.append(new_id[len(new_id)-1])
        answer=''.join(new_id) #리스트를 문자열로 변환
    return answer



new_id=(input())
answer=solution(new_id)
print(answer)