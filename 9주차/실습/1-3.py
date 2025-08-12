# https://www.acmicpc.net/problem/5597


all = set(range(1, 31))  # 1부터 30까지 학생 번호 집합

tw = set()               #제출한 학생들 집합

for _ in range(28):
    
    n = int(input())    #문자열로 입력받으니까 정수로 변환해야겠지?
    
    tw.add(n)

no = sorted(all -tw )

print(no[0])

print(no[1])
