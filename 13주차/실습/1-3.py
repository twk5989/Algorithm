def solution():
    n = int(input())                     # 수열의길이 입력
    tw = []                        #만들어야 하는 목표 리스트
    
    for _ in range(n):
        tw.append(int(input()))    # 한 줄씩 입력 받아 리스트에 저장

    stack = []        # 스택 역할을 할 리스트
    result = []       # 연산 결과 (+, -)를 저장할 리스트
    c = 1   #푸시를 할 시작점

   
    for num in tw:
        
        # 아직 목표 숫자까지 스택에 넣지 않았다면은
        while c <= num:
            stack.append(c)   
            result.append("+")      
            c += 1        

        #스택의 가장 위(top)가 내가 원하는 숫자여야 함
        if stack[-1] == num:
            stack.pop()             # pop 해서 목표 숫자 꺼냄
            result.append("-")      # 연산 기록
            
        else:
            # 스택 top이 내가 원하는 숫자랑 다르면 만들수가 업브음
            print("No")
            break
        
    print("/n".join(result))