# https://www.acmicpc.net/problem/2990


# 일단 단어의 갯수를 입력
n = int(input())

# 그 단어를 저장할 빈 문자열 DB
db = []

# 검색할 단어 개수를 입력
Q = int(input())

for _ in range(n): #n번 단어를 입력해서 단어를 db 배열에 넣음
    
    word = input()
    db.append(word)

# 1단계


def TW(a, b):
    
    i = 0 
    while i < len(a) and i < len(b) and a[i] == b[i]: #왜 이 조건을 이런식으로 적었는지 이해하는 시간을 가져보면 좋을 듯
        
        i += 1
        
    return i + 1  # 마지막까지 같거나 다를 때 비교 한 번 더 필요함



for _ in range(Q):
    search = input()   #검색할 단어의 갯수만큼 반복문을 또또 만들고 하나씩 입력해서 search에 넣음
                       #문자열끼리의 비교가 아닌 db의 문자열에서 입력값이랑 비교하는거니까 search는 db처럼 문자열을 안 만듬.
    C = 0  # 비교 횟수


    #모든 기본 셋팅을 끝내고 여기서부터 위의 함수 실행
    for ii in db: 
        count = TW(search, ii)
        C += count

        if search == ii:
            break  # 찾았으면 더 이상 비교 안 함

    print(C)
