#https://school.programmers.co.kr/learn/courses/30/lessons/388351

def solution(schedules, timelogs, startday):
    
    def m(t):   #일단 분으로 만드는 함수를 설정함
        return (t // 100) * 60 + (t % 100)  #950은 9시 50분이기에

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




#리팩토링 코드
def solution(schedules, timelogs, startday):
    
    answer = 0
    
    st = startday
    
    for x, y in enumerate(schedules): #x는 사람 번호 인덱스. y는 그 사람의 예정 출근시간
        
        tw = True  #이 사람이 출근에 성공여부.일단 True로 설정
        
        if y%100 >= 50: #이거를 왜 적었을까. 왜 내가 50을 더했을까 애들아?
            
            y += 50
            
        else:
            y += 10
            
        for i in timelogs[x]: #x번째 사람의 출근 기록 리스트와 i는 그 날의 실제 출근 시간
            
            if not i <= y and not 6 <= startday <= 7:
                tw = False
                break
            startday += 1 #그 날 검사 했으니. 그 다음날로 넘어감
            
            if startday == 8: #일주일은 7일이니 8일로 되면 1로 돌아감
                startday = 1
                
        if tw == True:
            answer += 1
        startday = st #다음사람 검사해야하니 초기화
        
    return answer

