# https://www.acmicpc.net/problem/2990

def TW(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]: #왜 이 조건을 이런식으로 적었는지 이해하는 시간을 가져보면 좋을 듯
        i += 1
        
    return i + 1  # 마지막까지 같거나 다를 때 비교 한 번 더 필요함

# 일단 단어의 갯수를 입력
n = int(input())

# 그 단어를 저장할 빈 문자열 DB
db = []


for _ in range(n): #n번 단어를 입력해서 단어를 db 배열에 넣음
    word = input()
    db.append(word)

# 검색할 단어 개수를 입력
Q = int(input())

for _ in range(Q):
    search = input()   #검색할 단어의 갯수만큼 반복문을 또또 만들고 하나씩 입력해서 search에 넣음
    C = 0  # 비교 횟수

    #모든 기본 셋팅을 끝내고 여기서부터 위의 함수 실행
    for ii in db: 
        count = TW(search, ii)
        C += count

        if search == ii:
            break  # 찾았으면 더 이상 비교 안 함

    print(C)


#리팩토링 버전
#접근 방식: 그 전에는 순차적으로 비교하며 찾아서 비교 횟수를 세어서 구현을 했었는데 그게 아닌 배열에서 내가 검색하고자하는 단어를 일단 찾고 처음-찾은 단어까지 잘라서 배열을 새롭게 만들자 

def TW(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i + 1 

n = int(input())

for _ in range(n):
    word = input()
    db.append(word)


Q = int(input())

for _ in range(Q):
    search = input()
    total = 0
    
    #찾을 위치를 미리 계산
    #근데 여기서 오해를 할 수 있음 5개 다 들어가는거 아니냐. 근데 위에 TW의 조건을 확인해 보시길
    index = db.index(search)
    
    for word in db[:index + 1]:
        total += TW(search, word)
        
    print(total)
