print('1부터 n까지 정수의 합을 구하시오')

n = int(input('n의 값을 입력하세요.:'))

sum = 0
for i in range(1, n + 1): 
    #range함수를 사용해서 반복으로 1부터 n까지의 숫자들을 i에 넣는다.
    sum += i

print(f'1부터 {n}까지의 정수의 합은 {sum}입니다')