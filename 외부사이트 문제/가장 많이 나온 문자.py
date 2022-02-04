import re ,collections
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
paragraph=paragraph.lower() #문자를 다 소문자로 바꾸기
check=re.findall(r'[a-z]+',paragraph)
print(check)
new=(collections.Counter(check).most_common()) #counter의 most_commom을 사용
#most_commom()을 사용하면 최대 사용값 순서대로 return 값이 나온다.
for i in new:
    if i[0] in banned:
        continue
    print(i[0])
    break
# for i in banned:
#     if i in check: