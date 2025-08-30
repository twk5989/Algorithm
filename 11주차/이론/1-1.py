# 고정 길이 스택 클래스 FixedStack 구현하기
from typing import Any

class FixedStack:

    class Empty(Exception): #비어있을 때의 예외처리
        pass

    class Full(Exception): #가득 차 있을때의 예외처리
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity  # 스택 본체
        self.capacity = capacity      # 스택의 크기
        self.ptr = 0                  # 스택 포인터

    def __len__(self) -> int: #스택에 모여있는 데이터 갯수를 반환
        return self.ptr

    def is_empty(self) -> bool: #스택이 비어있는지
        return self.ptr <= 0

    def is_full(self) -> bool: #스택이 가득 차 있는지
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():              # 스택이 가득 참
            raise FixedStack.Full
        
        self.stk[self.ptr] = value
        self.ptr += 1
 
    def pop(self) -> Any:  #꼭대기의 데이터를 꺼냄
        
        if self.is_empty():             # 스택이 비어 있음
             raise FixedStack.Empty
         
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:  #꼭대기의 데이터를 들여다 봄

        if self.is_empty():             # 스택이 비어 있음
            raise FixedStack.Empty
        
        return self.stk[self.ptr - 1]

    def clear(self) -> None:   #삭제
        self.ptr = 0

    def find(self, value: Any) -> Any:  #스택에서 value값을 찾는.
        
        for i in range(self.ptr - 1, -1, -1):  # 꼭대기부터 선형 검색
            
            if self.stk[i] == value:
                return i       #성공
            
        return -1              #실패

    def count(self, value: Any) -> bool:  #스택에 포함된 value 값을 반환

        c = 0
        for i in range(self.ptr):        #바닥부터 선형 검색
            
            if self.stk[i] == value:
                c += 1                   #있음
        return c

    def __contains__(self, value: Any) -> bool: #포함되어있는지 판단
        return self.count(value)

    def dump(self) -> None:   #스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력
      
        if self.is_empty():  # 스택이 비어 있음
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])