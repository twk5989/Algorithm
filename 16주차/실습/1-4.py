import sys

def solution():
    try:
        data = input().split()
        if not data:
            return
            
        N = int(data[0])
        K = int(data[1])
        
        A = list(map(int, input().split()))
        
    except EOFError:
        return
    except Exception:
        return

    swap_count = 0
    result_array = None

    for last in range(N, 1, -1):
        for i in range(last - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                
                swap_count += 1
                
                if swap_count == K:
                    result_array = list(A)
                    print(*(result_array))
                    return

    if result_array is None:
        print("-1")

solution()