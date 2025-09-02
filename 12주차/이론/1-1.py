# 고정 길이 큐 클래스 FixedQueue 구현하기
from typing import Any

class FixedQueue:

    #비어 있는 FixedQueue에대해 deque 또는 peek를 호출할 때 내보내는 예외처리
    class Empty(Exception):
        pass

    #가득 찬 FixedQueue에 enque를 호출할 때 내보내는 예외처리
    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:

        self.no = 0     # 현재 데이터 개수
        self.front = 0  # 맨앞 원소 커서
        self.rear = 0   # 맨끝 원소  커서
        self.capacity = capacity      # 큐의 크기
        self.que = [None] * capacity  # 큐의 본체

    #큐에 있는 모든 데이터 개수를 반환
    def __len__(self) -> int:
        return self.no
    
    #큐가 비어 있는지 판단
    def is_empty(self) -> bool:
        return self.no <= 0

    #큐가 가득 찼는지 판단
    def is_full(self) -> bool:
        return self.no >= self.capacity

# 데이터를 넣는 enque 함수
    def enque(self, x: Any) -> None:
        """데이터 x를 인큐"""
        if self.is_full():
            raise FixedQueue.Full  # 큐가 가득 찬 경우 예외처리를 발생
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

#데이터를 꺼내는 deque 함수
    def deque(self) -> Any:
        """데이터를 디큐합니다"""
        if self.is_empty():
            raise FixedQueue.Empty  # 큐가 비어 있는 경우 예외처리를 발생
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x


    #맨 앞 데이터를 들여다 봄
    def peek(self) -> Any:
        
        if self.is_empty():
            
            raise FixedQueue.Empty  # 큐가 비어 있으면 예외처리를 발생
        
        return self.que[self.front]

    #큐에서 value를 찾아 인덱스를 반환하고 없으면 -1을 반환합니다
    def find(self, value: Any) -> Any:
        
        for i in range(self.no):
            
            idx = (i + self.front) % self.capacity
            
            if self.que[idx] == value:  # 검색 성공
                
                return idx
            
        return -1  # 검색 실패

    #큐에 포함되어 있는 value의 개수를 반환합니다
    def count(self, value: Any) -> bool:
        
        c = 0
        
        for i in range(self.no):  # 큐 데이터를 선형 검색
            
            idx = (i + self.front) % self.capacity
            
            if self.que[idx] == value:  # 검색 성공
                
                c += 1  # 들어있음
                
        return c

    #큐에 value가 포함되어 있는지 판단합니다
    def __contains__(self, value: Any) -> bool:
        
        return self.count(value)

    #큐의 모든 데이터를 비웁니다
    def clear(self) -> None:
        
        self.no = self.front = self.rear = 0

    #모든 데이터를 맨 앞에서 맨 끝 순서로 출력합니다
    def dump(self) -> None:
        
        if self.is_empty():  # 큐가 비어 있으면 예외처리를 발생
            
            print('큐가 비어 있습니다.')
            
        else:
            for i in range(self.no):
                
                print(self.que[(i + self.front) % self.capacity], end=' ')
                
            print()