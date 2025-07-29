#1000 이하의 소수를 나열하기 (개선1)

counter = 0
ptr = 0
prime = [None] * 500                        #소수를 저장하는 배열

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):             #n의 값을 3부터 2씩 증가시켜 홀수의 값만 생성 => 4이상의 짝수는 2로 나누어 떨어지니까
    
    for i in range(1, ptr):             #ptr-1번 반복
        
        counter += 1
        if n % prime[i] == 0:
            break                       #여기 반복문은 지금까지 prim[i]의 i값 즉 지금까지 구한 소수로 나누기를 반복
        
    else:
        prime[ptr] = n
        ptr += 1
        
for i in range(ptr):
    print(prime[i])

print(f'나눗셈을 실행한 횟수: {counter}')