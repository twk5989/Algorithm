#나이를 입력 받아 성인인지 미성년자인지 판단하기 성인의 기준의 나이는 20살

def Taewoo(name, age):
    
    if age >= 20:
        print(f"{name}님은 성인입니다.")
        
    else:
        print(f"{name}님은 미성년자입니다.")



name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))


Taewoo(name, age)