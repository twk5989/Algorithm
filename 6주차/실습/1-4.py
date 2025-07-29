# 문제 설명
# 양의 정수 n이 매개변수로 주어집니다. 
# n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ n ≤ 30
 

def solution(n):
    if not isinstance(n, int):
        print("n은 정수여야 합니다.")
        
    if n < 1 or n > 30:
        print("n은 1 이상 30 이하의 정수여야 합니다.")

    arr = [[0] * n for _ in range(n)]

    # 방향
    dx = [0, 1, 0, -1] 
    dy = [1, 0, -1, 0]

    x, y = 0, 0 
    