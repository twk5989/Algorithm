# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    
    n = len(elements) #원소의 길이를 저장 왜냐하면 N개만큼 더해야하니까
    
    sum = set()  # 중복 제거.set은 
    
    answer = 0     #총 갯수

    for length in range(1, n + 1):         #수열의 길이를 정해서 반복해.예를 들어 배열이 [7,9,1]이라면 길이가 1일 때, 2일 때, 3일 때의 경우를 다 확인해야함.
        
        for TW in range(n):             #인덱스 원소: 시작 인덱스(TW)를 0부터 n-1까지 바꿔가며
            total = 0
            
            for i in range(length):        # 길이만큼 반복하며 합 계산
                total = total + elements[(TW + i) % n]
                # total += elements[(TW + i) % n] 
                
                
            if total not in sum:          #합이 sum에 없다면 중복이 없다는거니까
                
                sum.add(total)            #sum의 total값을 추가
                answer += 1                # 그에따른 answer 값 증가

    return answer #마지막은 sum의 배열의 len값을 출력해도 되지만 return answer을 지켜야하기에 출력



# 배열: [7,9,1], length=2, TW=1

# 합치고 싶은 부분 수열: [9, 1]

# i = 0: elements[(1 + 0) % 3] = elements[1] = 9

# i = 1: elements[(1 + 1) % 3] = elements[2] = 1

# 둘을 더해서 total = 10 계산
