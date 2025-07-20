# 사용자로부터 길이가 5 이상인 문자열 리스트를 입력받아,
# 가운데 3개의 원소만 슬라이스로 잘라 출력하세요.

words = input("입력: ").split()

n = len(words)

mid = n // 2

print(words[mid - 1 : mid + 2])

#start는 mid - 1이고 stop은 mid + 2, step은 생략이므로 1이다.