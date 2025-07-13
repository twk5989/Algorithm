# def는 python에서 함수를 정의할때 사용하는 것
def med3(a,b,c): #함수 이름이 middle(a,b,c)인것임. 그러니까 나중에 출력(print)할 때에도 저 이름 그대로 출력해야함
    
    if a > b: #1
        if b > c:
            return b
        elif a < c:
            return a
        else:
            return c
        
    elif a > c : #2 if a > b에서 거짓인 경우이니까 즉 a < b인 상황에서 a > c 인 조건까지 더해진것.
        return a
    
    elif b > c : #3 위 2개의 조건문을 둘다 만족하지 않는 것이기에 a < b, a < c인 상황 
        return c
    
    else:   # 나머지는 a < b, a < c, b < c인 상황임
        return b

print ('세 정수를 입력')

a= int(input('정수 a를 입력:'))
b= int(input('정수 b를 입력:'))
c= int(input('정수 c를 입력:'))

print(f'중앙값은 {med3(a,b,c)}입니다')