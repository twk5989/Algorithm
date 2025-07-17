area = int(input("직사각형의 넓이를 입력하세요"))

for i in range(1, area + 1):
    
    if i * i > area : break
    if area % i : continue         #area가 i로 나누어 떨어지지않는다면 i는 변의 길이가 될 수 없다
    print(f'{i} * {area // i }') 
    
    #이거는 직사각형의 넓이에 따른 변의 길이를 구하는 즉 약수를 구하는 것임
    
    