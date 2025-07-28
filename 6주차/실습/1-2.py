#이거는 앞의 문제를 바꾸어서 최댓값을 구하는게 아닌 교집합을 구하기

def app(A,B):
    
    common = []
    
    for a in A:
        for b in B: 
            if a == b and a not in common: 
                common.append(a)
    
    if len(common) == 0:
        print("공통원소가 없습니다")
        
    else:
        max = common[0]
        for i in range(1, len(common)):
            if common[i] > max:
                max = common[i]
                
        print(max)
                