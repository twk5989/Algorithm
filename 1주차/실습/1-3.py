# 세 정수를 입력 받고 중앙값 구하는 것

def middle(a,b,c): 
    
    if a > b: #1
        if b > c:
            return b
        elif a < c:
            return a
        else:
            return c
        
    elif a > c : #2 
        return a
    
    elif b > c : #3 
        return c
    
    else:   #나머지는
        return b
    
print('정수 3개를 입력하세요')

a = int(input('정수 a를 입력'))
b = int(input( '정수 b를 입력'))
c = int(input( '정수 c를 입력'))

print(f'중앙값은{middle}임')