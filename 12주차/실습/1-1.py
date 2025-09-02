# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    
    t = [] #이거는 이차원이 될 배열을 먼저 초기화
    index = 0
    
    for p in priorities:       #priorities 안의 값을 하나씩 꺼냄.
        
        pair = [index, p]      #[인덱스, 우선순위]형태로 만들어
        
        t.append(pair)         #위에서 만든 pair배열을 q에 넣어-> 그러면 이차원 배열이지?
        
        index += 1             #그리고 인덱스의 값은 하나씩 증가시켜.

    answer = 0
    
    #위의 이차원 배열 결과는 [[0,2],[1,1],[2,3]]이런식으로 나오겠지?


    while len(t) > 0:        #큐가 빌 때 까지 돌아가는 반복문 시작
        front = t.pop(0)
        i = front[0]   # 인덱스
        p = front[1]   # 우선순위

        # 뒤에 더 큰 우선순위가 있는지 확인하는 반복문 
        more = False
        
        for x in t:
            if x[1] > p:
                more = True
                break

        # 더 큰 게 있으면 뒤로 보냄
        if more == True:
            t.append([i, p])
            
        else:
            answer = answer + 1
            # 찾던 프로세스라면 종료
            if i == location:
                return answer