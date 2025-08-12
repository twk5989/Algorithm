# https://www.acmicpc.net/problem/2566

#일단 행과 열이니까 2차원으로 만들어야하고

max_rc = 0       #최댓값   

max_row = 0      #행  

max_col = 0      #열

for i in range(9):        #i는 행
    
    row = list(map(int, input().split()))  #내가 입력하는건 문자열로 인식되니까 정수형으로 변환해서 리스트를 만듬
    
    for j in range(9):     #j는 열
        
        #이해가 안될까봐 적어둘게 위에 for문은 총 9번 반복을해 열이 9개이니까
        #그리고 아래의 if문은 j가 9번 실행이되잖아. 한 행의 9개의 원소를 하나씩 확인한다는거야. 위에 또 for문이 있으니까그걸 총 9번 하는거고(81번)
         
        if row[j] > max_rc:  
            
            max_rc = row[j]
            
            max_row = i + 1   #여기 두개의 줄에 왜 +1을 적었을까 강찬아
            
            max_col = j + 1  

print(max_rc)

print(max_row, max_col)
