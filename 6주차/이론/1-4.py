# 기수 변환 2진수 8진수 16진수로 구하기. (10부터가 A임) p.89



def card_conv(x:int, r:int) -> str: #정수형 x와 r을 문자열로 변환
    
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    while x > 0:  #x를 r로 나눈 나머지 값을 dchar에서 찾아서 d에 이어 붙임 dchar[1] = 1
        d += dchar[x % r]
        x //= r 
    
    return d[::-1] #x가 0이 될때까지 무한 반복을하고 진수 출력을 위해 슬라이싱 문법으로 뒤집어서 출력시킴

if __name__ == '__main__': # 이 파일을 직접 실행 했을때에만
    print('10진수를 n 진수로 변환합니다')
    
    while True:
        #양의 정수를 입력할때에
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요:'))
            if no > 0:
                break #여기서는 no가 x에 대응
    
        while True:
          cd = int(input('어떤 진수로 변환할까요?:'))
          if 2 <= cd <= 36:
            break  #cd 가 r에 대응
        
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다') #위의 함수에 의해 결국 d를 return함
    
        retry = input('한번 더 하실?(Y............예 / N......아니요):')
        if retry in {'N', 'n'}:
            break