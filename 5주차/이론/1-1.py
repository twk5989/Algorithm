#학생의 점수를 입력 받아 합계와 평균 구하는 간단한 문제

print("학생 점수의 합계와 평균을 구한다.")

score1 = int(input("1번 학생의 점수를 입력"))
score2 = int(input("2번 학생의 점수를 입력"))
score3 = int(input("3번 학생의 점수를 입력"))
score4 = int(input("4번 학생의 점수를 입력"))
score5 = int(input("5번 학생의 점수를 입력"))

total = 0

total += score1
total += score2
total += score3
total += score4
total += score5

print("합계는 {total}입니다")
print(" 평균은 {total/5}입니다")