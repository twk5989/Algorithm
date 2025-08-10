#이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a:Sequence, key: Any )-> int:
    
    pl = 0             #검색 범위에서의 맨 앞 원소의 인덱스를 pl 지정
    pr = len(a) -1     #검색 범위에서 맨 뒤 원소의 인덱스를 pr 지정
    
    while True:
        pc = (pl +pr) //2   #원소의 중앙 인덱스를 pc로 지정
        if a[pc] == key:    #key는 우리가 찾으려는 값. a는 배열
            return pc       # 검색 성공
        
        elif a[pc] < key:
            pl = pc + 1    #키 값이 중앙 값보다 크다면 중앙값 기준 오른쪽에 있는 것이기에 시작점을 pc+1로 해야겠지?
            
        else:              #반대로 중앙값보다 작다면 그냥 반대로 하면되겠지?
            pr = pc -1
            
        if pl > pr:        #pl이 pr보다 커짐-> 값이 없다는거임 그럼 끝.
            break
        
    return -1           #검색 실패
    
if __name__ == '__main__':
        
    num = int(input('원소 수를 입력하세요'))
    x = [None] *num      #원소 수가 num인 배열을 생성
        
    print('배열 데이터를 오름차순으로 입력하세요')
        
    x[0] = int(input('x[0]: '))
        
    for i in range(1, num):        #num의 갯수만큼 원소의 값을 직접 입력하도록 반복문 설정
        while True:
            x[i] = int(input(f'x[{i}]: '))
                
            if x[i] >= x[i -1]:    #이 조건을 설정하면 리스트가 오름차순이 보장됨
                break
                
    ky = int(input('검색할 값을 입력하세요'))
        
    idx = bin_search(x, ky) #함수를 호출 x는 배열이고 ky는 찾고자하는 key값이겠지? 위에 함수 정의해놓은거 참고
        
    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.') #실패
            
    else:
        print(f'검색 값은 x[{idx}]에 있습니다')       #성공