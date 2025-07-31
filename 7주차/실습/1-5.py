#https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    
    answer = [] #실패율이 높은 순서대로 마지막에 반환할 스테이지 번호들
    total_players = len(stages)  # 전체 플레이어 수를 계산
    
    result = [] #실패율을 담을 리스트
    

    for stage in range(1, N + 1):
        # 현재 스테이지에 있는 사람 수 (아직 클리어 못한 사람)
        fail = stages.count(stage)

        # 실패율 계산부분.
        
        if total_players == 0: #실패율이 0일때
            faile_rate = 0
            
        else:
            faile_rate = fail / total_players


        result.append((stage, faile_rate)) #스테이지번호, 실패율을 result에 추가
        
        result.sort(stage, faile_rate)
        
        answer.append(stage)

    return answer
