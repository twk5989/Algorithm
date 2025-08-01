# 리스트 또는 튜플을 인자로 받아,
# 최댓값과 원소 개수를 출력하는 함수 analyze 를 작성하시오.

from typing import Sequence, Any

def analyze(data: Sequence[Any]) -> None: #반환하지 않는다 -> return을 하지않고 print 값만 출력한다.
    
    print("최댓값:", max(data))
    print("원소 개수:", len(data))
    



analyze((10, 20, 30))

analyze([5, 2, 9, 1])

