#1부터 n까지 정수의 합 구하기(인수가 이뮤터블 일때)

def sum_1ton(n):
    
    s = 0
    
    while n > 0:
        s  += n
        n -= 1
    return s

x = int(input('x의 값을 입력하세요:'))

print(f'1부터 {x}까지의 정수의 합은 {sum_1ton(x)}입니다')

#근데 문득 드는 생각 너무 당연하게 x 와 s 함수를 {}안에 담아서 코드를 작성하는데 왜 {}안에 적어야하는 걸까.
#이유는 생각보다 간단하다. x와 s 함수의 결과 값은 정수형다. 근데 {}안에 담아서 형변환을 시킨다
#즉 정수형을 -> 문자열로 변환시킨후 텍스트 문자들과 함께 출력시킨다.



#인수가 뮤터블일때

def tw(lst, idx, val):
    
    lst[idx] = val #이게 핵심 코드.
    
x = [11, 22, 33, 44, 55] #일단 x라는 리스트를 생성

print('x = ' ,x )

index = int(input('업데이트할 인덱스를 선택하세요'))
value = int(input('새로운 값을 입력하세요:'))

tw(x, index, value) 
#x 리스트를 lst매개변수로 전달,사용자가 입력한 index값을 idx로 전달, 사용자가 입력한 value값을 매개변수 val로 전달

print(f'x = {x}')