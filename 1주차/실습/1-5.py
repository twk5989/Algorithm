#숫자중 몇개가 양수인가?

def count_set(a,b,c): #함수정의
    count = 0 #갯수를 저장할 변수를 생성 및 초기화.처음이니까 0으로 초기화
    # count += 1
    if a > 0:
        count = count + 1
    if b > 0:
        count = count + 1
    if c > 0:
        count = count + 1
        
    return count



a = int(input('a의 숫자를 입력하세요'))
b = int(input('b의 숫자를 입력하세요'))
c = int(input('c의 숫자를 입력하세요'))

#굳이 이렇게 함수이름을 {count_set(a,b,c)}이렇게 넣는 것 보다는 result = count_positive(a, b, c)이런식으로 정의해서 넣어도 된다
print(f'양수는 {count_set(a,b,c)}개 입니다' )