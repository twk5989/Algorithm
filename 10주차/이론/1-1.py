# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        
        """초기화"""
        self.key   = key    # 키
        self.value = value  # 값
        self.next  = next   # 뒤쪽 노드를 참조



class ChainedHash:
    """체인법을 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity             # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity  # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

# Do it! 실습 3-5[C]

    #키가 key인 원소를 검색하여 값을 반환
    def search(self, key: Any) -> Any:

        hash = self.hash_value(key)  # 검색하는 키의 해시값
        
        p = self.table[hash]
        

        while p is not None:
        #p가 None이 아닐때까지(연결되 노드가 없을때까지)
        
            if p.key == key:
                 return p.value  # 검색 성공
             
            p = p.next           # 다르다면 뒤에 노드를 봄

        return None              # 결국 찾지못하면 실패


    # 키가 key이고 값이 value인 원소를 삽입
    def add(self, key: Any, value: Any) -> bool:
        
        hash = self.hash_value(key)  
        p = self.table[hash]         

        while p is not None:
            if p.key == key:
                return False         
            p = p.next               

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp     
        return True                  

    #키가 key인 원소를 삭제
    
    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)
        p = self.table[hash]        
        pp = None                    

        while p is not None:
            if p.key == key:  
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True  
            pp = p
            p = p.next      
        return False         

    #해시 테이블을 덤프
    
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  → {p.key} ({p.value})', end='')  # 해시 테이블에 있는 키와 값을 출력
                p = p.next
            print()