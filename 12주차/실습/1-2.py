# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    
    answer = []
    
    if not arr:
        return answer
    
    #쉽게 이야기하자면 arr에서 answer로 하나씩 옮긴다고 생각하면 될 듯
     
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        
        if arr[i] != arr[i-1]:
            
            answer.append(arr[i])
            
    return answer