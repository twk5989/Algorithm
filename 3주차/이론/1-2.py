print('a부터 b까지의 정수의 합을 구한다')

a = int(input('정수 a를 입력'))
b = int(input('정수 b를 입력'))

if a > b:
    a, b=b, a
    
sum = 0

#교환(swap)문법. a를 먼저 입력하는데 a가 b보다 크다면 b가 먼저오고 a가 나중에 온다
for i in range(a, b+1): 
    sum += i
    
print(f'{a}부터  {b}까지 정수의 합은 {sum}입니다')