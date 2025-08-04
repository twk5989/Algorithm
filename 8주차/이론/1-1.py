#while문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:   #a는 우리가 탐색할 리스트이고 key는 찾을 값이다.
                                                #반환형은 정수이다. 실패하면 -1이고 성공하면 인덱스출력
    i = 0       #탐색을 시작할 인덱스를 0으로 시작-> 처음부터 순차적으로 찾아봐야하기에                               
    
    while True:
        
        if i == len(a): # i가 인덱스의 끝에 도달했는지
            return -1
        
        if a[i] == key:
            return i
        
        i += 1
        
if __name__ == '__main__':
    
    num = int(input('원소 수를 입력하세요'))
    
    x = [None] * num #길이가 num인 리스트 x를 생성
    
    for i in range(num): #num의 길이만큼 반복을 실행하여 x의 원소값을 대입시킴
        x[i] = int(input(f'x[{i}]: '))
        
    ky = int(input('검색할 값을 입력하세요'))
    
    idx = seq_search(x, ky)
    
    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다')
        
    else:
        print(f'검색값은 x[{idx}]에 있습니다')