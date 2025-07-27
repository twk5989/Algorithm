#여기는 1-4의 코드를 수정해서 기수변환 과정을 자세히 나타냄

def card_conv(x:int, r:int) -> str:
    
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))       #변환하기 전의 자릿수
    
    print(f'{r:2} | {x:{n}d}')
    