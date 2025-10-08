# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    
    n = len(citations)
    
    answer = 0
    
    for i in range(n):
        
        h = i + 1
    
        if citations[i] >= h:
            
            answer = h
        else:
           break
            
    return answer


def solution(citations):
    citations.sort(reverse=True)

    for i, c in enumerate(citations): #c는 인용수
        if c < i + 1:
            
            return i
    
    return len(citations)
