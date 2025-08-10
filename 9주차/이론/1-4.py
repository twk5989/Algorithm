from typing import Any, Sequence                  #Sequence는 리스트/튜플 등 순서 있는 컨테이너를 의미하고, Any는 모든 타입 허용을 나타냅니다

def bin_search(a: Sequence, key: Any) -> int:     #최종 마지막에 정수형으로 반환한다(int)
    pl = 0            #시작 인덱스 
    pr = len(a) - 1   #맨 마지막 인덱스

    print(' |', end='')   #출력될때 정렬을 맞추기 위한 print문.
    
    for i in range(len(a)):   #a의 길이만큼 반복해서 아래 print문을 출력
        print(f'{i:4}', end='') #폭이 4킨이고 오른쪽 정렬로 출력이 됩니다.end는 같은 줄에 이어서 출력된다.
        
    print()
    
    print('---+' + (4 * len(a) + 2) * '-') #구분선을 출력합니다.

    if not a:               # 빈 스퀸스는 False로 평가되죠 그렇기에 not a는 True로 평가 됩니다. 그렇기에 True로 평가되면 리스트가 비어있다고 생각하여 -1을 출력하는겁니다.
                            # False는 리스트에 값이 있다. 그러니 검색을 시도해보겠다 이렇게 해석됩니다.
        return -1

    #메인 루프입니다.
    
    while pl <= pr:
        pc = (pl + pr) // 2

        # 화살표(포인터) 라인 출력
        print('   |', end='')

        if pl != pc:
            # pl 쪽에 '<-' 표시, pc 위치에 '+' 표시
            print(' ' * (pl * 4 + 1) + '<-' + ' ' * ((pc - pl) * 4 - 1) + '+', end='')
            
        else:
            # pl == pc 인 경우 간단히 '<+' 표시
            print(' ' * (pc * 4 + 1) + '<+', end='')

        if pc != pr:
            print(' ' * ((pr - pc) * 4 - 2) + '->')
            
        else:
            print('->')


        print(f'{pc:3}|', end='') #pc를 폭 3칸으로 정렬해서 출력, 뒤에 이어서 출력함.
        
        for i in range(len(a)):
            print(f'{a[i]:4}', end='')  #각 요소는 촉 4칸으로 오른쪽 정렬이 되어서 배열 요소들이 한줄로 출력이 된다.
            
        print('\n   |') #한 배열이 출력되고 나면 줄을 바꾸고 세칸공백+ | 를 출력

        # 실제 이진 검색 비교 및 범위 축소
        
        if a[pc] == key:          #key는 우리가 찾으려는 값, a는 배열
            return pc             #검색 성공
         
        elif a[pc] < key:
            pl = pc + 1            #키 값이 중앙 값보다 크다면 중앙값 기준 오른쪽에 있는 것이기에 시작점을 pc+1로
            
        else:
            pr = pc - 1            #pl이 pr보다 커짐-> 값이 없다는거임 그럼 끝.

    return -1                      #검색 실패


if __name__ == '__main__':
    
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num               #원소의 수가 num인 배열을 생성

    print('배열 데이터를 오름차순으로 입력하세요')
    
    x[0] = int(input('x[0]: '))    #인덱스 0값을 입력

    for i in range(1, num):        #num의 갯수만큼 원소의 값을 직접 입력하도록 반복문 설정
        while True:
            x[i] = int(input(f'x[{i}]: '))
            
            if x[i] >= x[i - 1]:   #이 조건을 설정하면 리스트가 오름차순으로 보장됨
                break

    ky = int(input('검색할 값을 입력하세요: '))
    
    idx = bin_search(x, ky)        #이제 여기서 위에 정의한 함수를 호출. x는 배열이고 ky는 내가 찾는 key값이다

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')           #실패
        
    else:
        print(f'검색 값은 x[{idx}]에 있습니다')                  #성공
