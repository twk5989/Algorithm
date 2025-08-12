# https://school.programmers.co.kr/learn/courses/30/lessons/181835

def solution(arr, k):
    
    answer = []
    
    if k % 2 == 1:  # k가 홀수일 때
        
        for x in arr:
            answer.append(x * k)
            
    else:  # k가 짝수일 때
        
        for x in arr:
            answer.append(x + k)
            
    return answer


#append는 arr라는 리스트에서 ()안의 원소값을 하나씩 추가하는 역할 