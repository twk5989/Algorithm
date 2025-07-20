#스퀸스를 이용해서 원소의 최댓값을 구하기
#들여쓰기 행과 열 조심

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    
    max = a[0]

    for i in range(1, len(a)):
    
        if a[i] > max:
            max = a[i]
        
    return max

if __name__=='__main__':
    
    print('배열의 최댓값을 구합니다')
    
    num = int(input('원소의 수를 입력하시오'))
    
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요'))
        
        
    print(f'최댓값은 {max_of(x)}입니다')
    
    
    
#스퀸스의 이론적인 부분은 노션에 작성할 예정