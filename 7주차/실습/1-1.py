#https://school.programmers.co.kr/learn/courses/30/lessons/181895

def solution(arr, intervals):
    answer = []
    
    #첫번째 구간
    a1, b1 = intervals[0]
    answer += arr[a1:b1 + 1]

    #두번째 구간
    a2, b2 = intervals[1]
    answer += arr[a2:b2 + 1]

    return answer

