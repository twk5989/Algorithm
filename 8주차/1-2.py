# while문이 아닌 for 문으로 작성

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    
    for i in range(len(a)):  #a의 배열 길이만큼 반복
        
        if a[i] == key:
            return i  #검색 성공시 인덱스를 반환
        
    return -1         #실패시 -1을 반환