# 문제 설명
# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# dots의 길이 = 4
# dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
# 0 ≤ x, y ≤ 100
# 서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
# 두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
# 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.



def solution(dots):
    if len(dots) != 4:
        print("dots는 정확히 4개의 점을 포함해야 합니다.")
        

    # 중복된 점이 있는지 확인하는거
    #TW = set()           #python의 내장형 함수 set을 사용해서 중복을 확인 TW에 하나씩 넣어보면서 확인하는 것이라네요
    
    for point in dots:
        if len(point) != 2:
            print("각 점은 [x, y] 형식이어야 합니다.")
        x, y = point #
        
        if not isinstance(x, int) or not isinstance(y, int):
            print("x, y는 정수여야 합니다.")
        
        if not (0 <= x <= 100 and 0 <= y <= 100):
            print("x, y는 0 이상 100 이하 정수여야 합니다.")
        
        # if tuple(point) in TW:
        #     raise ValueError("점이 서로 겹치면 안 됩니다.")
        # TW.add(tuple(point))

    
    def rldnfrl(p1, p2):  #기울기 계산 함수 부분
        x = p2[0] - p1[0]
        y = p2[1] - p1[1]
        
        if x == 0:
            print("y축과 평행한 직선은 안됨.")
        if y == 0:
            print("x 축과 평행한 직선도 안됩니도")
        return y / x

    #가능한 경우의 수 들
    if rldnfrl(dots[0], dots[1]) == rldnfrl(dots[2], dots[3]):
        return 1
    
    if rldnfrl(dots[0], dots[2]) == rldnfrl(dots[1], dots[3]):
        return 1
    
    if rldnfrl(dots[0], dots[3]) == rldnfrl(dots[1], dots[2]):
        return 1
    
    else:
        return 0
