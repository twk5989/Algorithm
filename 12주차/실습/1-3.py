# https://www.acmicpc.net/problem/10845


import sys

def solution():
    
    input = sys.stdin.readline
    
    n = int(input())           
    
    t = []                    
    
    front = 0  
    
    for _ in range(n):
        
        git = input().split() #그러면 이제 여기서 git의 구조가 어떻게 될까.
        
        if git[0] == "push":
            t.append(int(git[1]))
            
        elif git[0] == "pop":
            
            if front < len(t):
                print(t[front])
                front += 1
                
#front를 사용해서 큐의 현재 맨 앞의 원소를 출력. 근데 0을 적어버리면 리스트의 첫번째 원소를 출력. 큐의 앞이랑 다를수도 있음.
# 이미 맨앞을 front로 지정해서 하는거면 0으로 적을 것이 아닌 front로 지정해서 계속 쓰는게 맞다
            else:
                print(-1)
                
        elif git[0] == "size":
            print(len(t) - front)
            
        elif git[0] == "empty":
            
            if front < len(t):
                print(1)
                
            else:
                print(0)
            
        elif git[0] == "front":
            
            if front < len(t):
                print(t[front])
                
            else:
                print(-1)
                
        elif git[0] == "back":
            
            if front < len(t):
                print(t[-1])
                
            else:
                print(-1)


