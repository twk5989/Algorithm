# 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.

# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.
# 세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.



while True: #조건을 만족하기전까지 무한 반복
    
    sides = list(map(int, input("세 변의 길이를 입력하세요: ").split()))
    #split은 공백을 기준으로 문자열을 리스트로 만든다.=>["3", "4", "5"]
    #map함수와 int는 내가 입력한 3 4 5의 문자열을 정수형으로 변환해준다 => [3, 4, 5] 이후 map의 객체를 list로 변환
    
    if sides == [0, 0, 0]:  # 종료 조건
        break

    sides.sort()  #sides를 오름차순으로 정렬.

    a, b, c = sides

    if a + b <= c:
        print("Invalid")
        
    elif a == b == c:
        print("Equilateral")
        
    elif a == b or b == c or a == c:
        print("Isosceles")
        
    else:
        print("Scalene")

