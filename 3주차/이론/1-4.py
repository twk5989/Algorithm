print('*을 출력합니다')

n = int(input('몇 개를 출력 할까요?'))
w = int(input('몇 개마다 줄 바꿈을 할까요?'))

for i in range(n):
    print('*', end='')
    
    if i % w == w-1: # i를 w로 나눈 나머지가 w-1일 일때에 줄을 바꾼다(ex= w가 4이면 i는 3,7,11 일때에 줄을 바꾼다)
        print()
        
if n % w:  #n이 w의 배수라면 마지막 *을 출력하고 줄 바꿈.
    print()