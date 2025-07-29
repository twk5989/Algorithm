# 문제 두 리스트의 교집합 중 가장 큰 수 구하기
# 두 개의 리스트 A, B가 주어질 때, 공통으로 포함된 정수들 중 가장 큰 수를 찾아 출력하세요.
# 단, 중복은 제거하고 **순차 탐색(루프)**만 사용해서 풀어야 합니다.


def solution(A,B):
    
    common = []
    
    for a in A:
        for b in B: 
# 이부분 틀림. 이렇게 사용하는 이유는 A의 값하나에 B의 모든 값을 비교하기 위해서 사용. 
# 무슨 말이냐 승원이를 위해 더 자세히 설명해드림. A리스트 원소가 [1,2,3] B리스트 원소가[3,4,5]라고 가정 A가 1일때 B의 값에서 같은게 있나 하나씩 비교하며 찾는다고 생각하면돼
            if a == b and a not in common: #이 부분도 틀렸음. a not in common은 이미 추가된 값은 다시 넣지 않기위한 중복 제거용 조건
                common.append(a)
    
    if len(common) == 0:  #리스트 common안에 갯수가 0일때
        print("공통원소가 없습니다")
        
    else:
        max_val = common[0]
        
        for i in range(1, len(common)): #근데 여기서 왜 0이 아니고 1로 시작을 했을까?
            if common[i] > max_val:
                max_val = common[i]
                
        print(max_val)