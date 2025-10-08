# https://school.programmers.co.kr/learn/courses/30/lessons/120808

#1.일단 분자 분모를 정의 해야되고
#2.그 다음 최대 공약수를 구하는 함수를 정의해
#3.그리고 정의한 분자 분모를 최대공약수 함수에 대입 

def solution(numer1, denom1, numer2, denom2): #함수 정의
    
    T = numer1 * denom2 + numer2 * denom1#두 분수의 합을 구할때에는 분모 = 각 분모끼리 곱함. 분자 = 분자1*분모1 + 분자2*분모2 알지?
    W = denom1 * denom2    


    def rlaxodn(a, b):#최대공약수를 구하는 함수
        
        while b != 0:
            a, b = b, a % b
        return a

    kim = rlaxodn(T, W)

    # 기약분수로 만들어
    T //= kim
    W //= kim

    answer = [T, W]
    
    return answer