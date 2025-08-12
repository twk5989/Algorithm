# https://www.acmicpc.net/problem/2566

#일단 행과 열이니까 2차원으로 만들어야하고

max_rc = 0       #최댓값   

max_row = 0         #행  

max_col = 0      #열

for i in range(9):    # 0부터 8까지, 9개의 행
    
    row = list(map(int, input().split()))  # 한 줄에 9개 숫자 입력받기
    
    for j in range(9):  # 0부터 8까지, 9개의 열
        
        if row[j] > max_rc:
            max_rc = row[j]
            
            max_row = i + 1   # 인덱스가 0부터이므로 +1
            
            max_col = j + 1   # 인덱스가 0부터이므로 +1

print(max_rc)

print(max_row, max_col)
