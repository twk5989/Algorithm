def card_conv(x:int, r:int) -> str: #정수형 x와 r을 문자열로 변환
    
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    if x == 0:
        print("잘못쓴듯 0은 안된다고.")
        return '0'
    
    while x > 0:  #x를 r로 나눈 나머지 값을 dchar에서 찾아서 d에 이어 붙임 dchar[1] = 1
        d += dchar[x % r]
        x //= r 
    
    return d[::-1] #x가 0이 될때까지 무한 반복을하고 진수 출력을 위해 슬라이싱 문법으로 뒤집어서 출력시킴


def count(numbers: list[int], base: int, uni: str) -> int: #최종적으로 정수형 값을 반환한다 ㅇㅋ?
    count = 0
    
    for TW in numbers:  #설명하는 것도 지겹다. numbers에서 원소값을 하나씩 가져와 TW에 할당한다.
        converted = card_conv(TW, base) #함수 변환을 위해 converted
        
        if uni in converted:
            count += 1
    return count






#count_with_uni([10, 31, 255, 100], 16, 'F')  
# 10 → 'A' (X)  
# 31 → '1F' (O)  
# 255 → 'FF' (O)  
# 100 → '64' (X)  
#결과: 2
