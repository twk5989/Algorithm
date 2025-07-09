#세 사람중 가장 막내는?
def person (a1,a2,b1,b2,c1,c2): #함수 정의
    if a1 > b1 :
        if b1 > c1:
            return c2
        elif a1 > c1:
            return b2
        else:
            return b2
        
    elif a1 > c1:
        return c2
    
    elif b1 > c1:
        return a2
    
    else:
        return a2
    
print ('세 사람의 나이와 이름을 입력하세요')

a2 = input('a2의 이름을 입력하세요')
a1 = int(input('{a2}의 나이를 입력하세요'))
b2 = input('b2의 이름을 입력하세요')
b1 = int(input('{b2}의 나이를 입력하세요'))
c2 = input('c2의 이름을 입력하세요')
c1 = int(input('{c2}의 나이를 입력하세요'))

print(f'세 사람중 가장 나이가 어린 사람은 {person (a1,a2,b1,b2,c1,c2)} 입니다')