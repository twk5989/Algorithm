# https://school.programmers.co.kr/learn/courses/30/lessons/120808

def solution(numer1, denom1, numer2, denom2): #함수 정의
    
    T = numer1 * denom2 + numer2 * denom1
    W = denom1 * denom2    #두 분수의 합을 구할때에는 분모 = 각 분모끼리 곱함. 분자 = 분자1*분모1 + 분자2*분모2 알지?


    def rlaxodn(a, b):
        
        while b != 0:
            a, b = b, a % b
        return a

    kim = rlaxodn(T, W)

    # 기약분수로 만들어
    T //= kim
    W //= kim

    answer = [T, W]
    
    return answer
