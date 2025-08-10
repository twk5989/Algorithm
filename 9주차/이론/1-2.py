#선형 검색의 시간 복잡도 

def seq_search(a: Sequence, key: Any) -> int:
    i = 0                    #1

    while i < n:             #2
        
        if a[i] == key:      #3
            return i         #4
        i += 1               #5
        
    return -1                #6