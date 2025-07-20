# 리스트 또는 튜플을 인자로 받아,
# 최댓값과 원소 개수를 출력하는 함수 analyze 를 작성하시오.

from typing import Sequence, Any

def analyze(data: Sequence[Any]) -> None: #함수 정의해서 data(정보의 이름)로 정보가 함수에 입력
    # None= 이 함수가 어떠한걸 반환하지는 않는다.그냥 출력값만 표시한다라는 의미임
    
    print("최댓값:", max(data))
    print("원소 개수:", len(data))


analyze([5, 2, 9, 1])
analyze((10, 20, 30))
