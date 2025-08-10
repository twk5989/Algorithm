#이진 검색의 시간 복잡도

def bin_search(a: Sequence, key: Any) -> int:
    
    pl = 0                       #1
    pr = len(a) -1               #2
    
    while True:                  
        pc = (pl + pr) // 2      #3
        
        if a[pc] == key:         #4
            return pc            #5
        
        elif a[pc] < key:        #6
            pl = pc + 1          #7
            
        else:                    
            pr = pc -1           #8
        
        if pl > pr:              #9
            break        
        
    return -1                    #10