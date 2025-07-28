#여기는 1-4의 코드를 수정해서 기수변환 과정을 자세히 나타냄

def card_conv(x:int, r:int) -> str:
    
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))       #변환하기 전의 자릿수
    
    print(f'{r:2} | {x:{n}d}')
    while x > 0:
        print('  +' + (n + 2) * '-')
        
        if x // r:
            print(f'{r:2} | {x // r:{n}d}.....{x % r}')
        else:
            print(f'        {x // r:{n}d}.....{x % r}')
        d += dchar [x % r]
        x //= r
        
    return d[::-1] # 역순으로
        