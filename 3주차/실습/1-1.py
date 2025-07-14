# 짝수의 합만 구하기

n = int(input("몇번째까지 짝수의 합을 구할까요: "))
sum = 0

for i in range(1, n + 1):
    
    if i % 2 == 0:  # 짝수인 경우
        sum += i

print("짝수의 합:", sum)
