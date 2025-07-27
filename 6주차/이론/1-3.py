# 이터러블
# 문자열, 리스트, 튜플, 집합 등의 자료형 객체들은 모두 이터러블(반복)이 가능하다.
# 이터러블 객체는 원소를 하나씩 꺼내는 구조임. 


#배열을 역순으로 정렬하는 알고리즘 생각해보면 간단함.
# n//2번 만큼 반복문을 실행하고 a[i] 번째와 a[n - i -1]번째를 서로 교환하면됨

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None: #함수가 리스트 자체를 직접 변경하기에 어떤 값도 반환하지않는다(None)라고 정의함
    #reverse_array 함수의 매개변수 a가 MutableSequence 타입임을 명시
    
    n = len(a)
    for i in range(n //2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
        
if __name__ == '__main__':
    print('배열을 역순으로 정리')
    nx = int(input("원소의 수를 입력하세요"))  #nx의 변수에 저장을 하고 nx는 길이가 된다
    x = [None] * nx #원소의 수가 nx인 리스트x를 생성함
    
    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요:'))
        
    reverse_array(x) #x를 역순으로 정렬
    
    print('배열의 원소를 역순으로 정렬했습니다')
    for i in range(nx):
        print(f'x[{i}] = x[{i}]')
        
        
        
#__name__ = 모듈이름을 나타내는 변수, __name__ == __main__ => 내가 직접 이 py을 실행했을때 True임. 다른 스크립트에서 import해서 사용하면 False가 된다
        
        
        
#리스트를 역순으로 정렬하고 싶다면 reserved를 사용하면됨.
#예를 들어 리스트 x를 역순으로 정렬하여 y에 대입하려면

# y = list(reserved(x))를 하면된다.