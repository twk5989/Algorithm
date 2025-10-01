#https://school.programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    
    answer = []

    def move(no, x, y): #no개의 원판을 x기둥에서 y기둥으로 옮겨라
        
        if no == 0:
            
            return #끝난거지
        
        move(no - 1, x, 6 - x - y)   #move(1,1,2)-> (0.1.3)->(0.2.3)
        
        answer.append([x, y])       
        
        move(no - 1, 6 - x - y, y)   #move(1,2,3)

    move(n, 1, 3)
    
    return answer
