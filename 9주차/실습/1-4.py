# https://school.programmers.co.kr/learn/courses/30/lessons/388351

def solution(schedules, timelogs, startday):
    
    def m(t):   #일단 분으로 만드는 함수를 설정함
        return (t // 100) * 60 + (t % 100)

    n = len(schedules)  #n은 사원수임
    
    time = []           #설정값 +10을 해줄 time
    
    for s in schedules:
        time.append(m(s) + 10)

    answer = 0 
    # 1단계 끝
    
    
    
    
    for i in range(len(schedules)): #n을 적어도 상관없지
        
        for d in range(7):
            
            day = (startday - 1 + d) % 7 + 1 
            
            if day in (6, 7):
                continue
            
            if m(timelogs[i][d]) > time[i]:

                break
            
        else:
            answer += 1

    return answer