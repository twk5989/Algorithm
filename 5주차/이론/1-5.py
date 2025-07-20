#배열 원소의 최댓값을 구해서 출력하기(원소를 입력 받아서)

from max import max_of

print('배열의 최댓값을 구함')
print('주의: : "end"를 입력하면 종료됨')

number = 0
x= []

while True:
    s = input(f'x[{number}]값을 입력하세요')
    if s == "end":
        break
    
    x.append(int(s))
    number += 1
    
print(f'{number}개를 입력했음')

print(f'최댓값은 {max_of(x)}개 입니다')
