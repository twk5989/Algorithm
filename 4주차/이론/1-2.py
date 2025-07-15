# 이중 루프로 구구단을 출력

print('-' * 27) #여기서 27은 구분선이다

for i in range(1,10): #행 루프
    
    for j in range(1,10): #열 루프
        print(f'{i * j:3}', end='') #:3은 3칸의 너비를 맞춰서 출력하라는 의미임
    print()
    
print('-', * 27)