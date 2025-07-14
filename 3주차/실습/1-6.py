#1부터 n까지 중에서 3의 배수이면서 홀수인 수의 합을 구하기
#1-3을 응용해서 풀 수 있음.
#n의 값을 입력하는 필드 작성 필수

n = int(input("n까지 곱할 정수를 입력하세요: "))

result = 1 #초기값은 1로 설정 곱해야하니까

TW = ""
valid = False  # 조건에 맞는 값이 있는지 추적

for i in range(1, n + 1):
    if i % 2 == 0 and i % 4 == 0: #짝수이면서 4의 배수일때
        value = i * 2 #값에 2를 곱함
        result *= value #최종 결과값은 더하기가 아닌 곱하기
        valid = True
        TW += f"*({i}*2)"
    
    elif i % 2 == 1 and i % 3 == 0:
        value = i - 1
        result *= value
        valid = True
        TW = f"*({i}-1)"

# 조건에 맞는 값이 하나도 없었다면 결과를 0으로 처리
if not valid:
    result = 0
    print("조건에 맞는 값이 없습니다. 결과: 0")
    
else:
    print(f"{TW} = {result}")
