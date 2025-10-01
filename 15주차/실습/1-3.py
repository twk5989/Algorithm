# https://www.acmicpc.net/problem/1966

import sys
input = sys.stdin.readline

#접근 방식. 일단은 갯수.위치(큐).중요도를 각각 배열로 일단 만들고
#갯수는 별로 안중요하니 인덱스,중요도 두개를 묶어서 큐 배열로 만든 뒤, 큐 배열에서 pop으로 하나씩 순차적으로 꺼내되, 꺼내면서 중요도를 비교
#중요도를 비교하는데 뒤에 더 중요한게 있으면 그걸 그냥 맨뒤로 보냄. 그걸 반복하다보면 언젠간 순차적으로 출력됨

T = int(input().strip())

for _ in range(T):
    
    N = map(int, input().split())
    M = map(int, input().split())
    im = list(map(int, input().split()))  #중요도

    # 큐
    q = []
    for i in range(N):
        q.append([i, im[i]]) #문서의 인덱스 번호랑 중요도를 묶어서 이중배열

    count = 0

    while True:
        cu = q.pop(0)              #그러면 cu은 [인덱스 위치,중요도]이 배열인거지
        cu_idx = cu[0]
        cu_p  = cu[1]

        #근데 뒤에 이것보다 중요한게 있을 수도 있잖아
        higher = False
        
        for t in range(len(q)): #큐에 남은 갯수만큼 다 확인해
            if q[t][1] > cu_p:
                
                higher = True
                break

        if higher:
            # 뒤에 더 높은 게 있으니 맨 뒤로 보냄
            q.append(cu)
            
        else:
            printed += 1
            if cu_idx == M:
                
                print(count)
                break