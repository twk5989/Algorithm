# 세 정수의 최댓값 구하기

def max3(a,b,c):
    
    maxim = a
     
    if b > maxim: maxim = b
    
    if c > maxim: maxim = c
    
    return maxim #최댓값을 반환

print(f'max3(3,2,1) = {max3(3,2,1)}')

#print(f'최댓값은 {maxim}입니다')
