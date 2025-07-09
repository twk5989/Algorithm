number = int(input())

answer = 0

for i in range(1): #여기를 while number > 0 :
    answer += number % 100
    number //= 100

print(answer)