# 홀수의 값은 더하고 짝수의 값은 빼기

n = int(input("너가 원하는 정수를 입력하세요: "))
result = 0

for i in range(1, n + 1):
    
    if i % 2 == 1:  # 홀수인 경우
        result += i
        
    else:  # 짝수인 경우
        result -= i   #result = result - i

print("결과는:", result)
