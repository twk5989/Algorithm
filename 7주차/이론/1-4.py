#1000 이하의 소수를 나열하기 (개선2)

counter = 0                         #여기서 counter는 곱셈과 나눗셈을 더한 값이다.
ptr = 0 #prime 리스트에 현재까지 저장된 소수의 개수를 나타내고, 동시에 다음 소수가 저장될 인덱스를 가리킵니다.
prime = [None] * 500 # 찾은 소수들을 저장할 리스트입니다

prime[ptr] = 2                      
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1   #prime[1] = 3. 3부터 시작해서 나누어보겠다는 말
    
    #여기의 while문이 성립하는 경우는 counter에 2를 더함.  ->곱하기,나누기의 카운트이기에
    while prime[i] * prime[i] <= n:
        counter += 2
        
        #while문 성립하지않는경우. 곱하기는 진행되지않고 나눗셈만 진행되기에 1을 더한다
        
        if n % prime [i] == 0:     #나머지가 0. 즉 나누어 떨어지면 소수가 아니다.
            break
        
        i += 1
    else:                          #마지막까지 나누어지지않는다면 소수.
        prime[ptr] = n             #소수배열(prime)에 n의 값을 등록
        ptr += 1
        counter += 1
        
for i in range(ptr):
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')
