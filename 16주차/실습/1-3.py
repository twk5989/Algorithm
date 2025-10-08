# https://www.acmicpc.net/problem/23969
#접근방식 1. 일단 문제에 맞는 몇개를 몇번 스위치할지 입력 필드 만들고
#2.넣을 숫자를 배열로 만들고 ture false로 조건문 만들어서 
#3.책에서 한대로 해보기

import sys

def main():
    input = sys.stdin.readline
    
    T, W = map(int, input().split())
    
    A = list(map(int, input().split()))

    count = 0
    
    for last in range(T - 1, 0, -1):
        
        change = False
        
        for i in range(last):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                
                count += 1
                
                change = True
                
                if count == W:
                    print(' '.join(map(str, A))) #문자열로 변환해서 공백으로 붙이기
                    return
        
        if not change:
            break

    # 여기까지 왔으면 총 교환 횟수 < K
    print(-1)


    
    
    