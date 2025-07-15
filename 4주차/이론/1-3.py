#일반적인 직각 이등변 삼각형(왼쪽 아래가 직각)

print('왼쪽 아래가 직각 이등변 삼각형을 출력')
n = int(input('짧은 변의 길이를 입력'))

for i in range(n):
    for j in range(i + 1):
        print('*', end= '')
    
    print()
    

#반대로 오른쪽 아래가 직각인 직각 이등변 삼각형

for i in range(n):
    for j in range(n-i-1):            #여기는 공백을 출력
        print('', end= '')
        
    for j in range(i +1):             #여기는 *을 출력
        print('*', end= '')
        
    print() 