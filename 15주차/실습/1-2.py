# https://www.acmicpc.net/problem/3003

#접근 방식: 기준점을 세워서 (기준점)- (사용자가 갖고 있는 갯수) = 배열 출력


#처음에는 정확한 갯수의 배열을 만듬(기준)
chess = [1, 1, 2, 2, 2, 8]

#그 다음 입력 필드 및 배열 생성
c = list(map(int, input().split())) 

#그다음 결과값 배열 생성
result = []

for i in range(6):
    
    result.append(chess[i] - c[i])


print(*result)
