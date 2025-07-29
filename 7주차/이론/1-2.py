# 1000이하의 소수 나열하기

counter = 0

for n in range(2, 1001):          #n은 판별할 대상의 숫자
    
    for i in range(2,n):          #i는 나눌 숫자
        counter += 1
        
        if n % i ==0:             #나누어 떨어지면 소수가 아님
            break
        
    else:                         #끝까지 나누어 떨어지지않으면 else를 실행
        print(n)
print(f'나눗셈을 실행한 횟수: {counter}')