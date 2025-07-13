#나이를 입력 받아 성인인지 미성년자인지 판단하기 성인의 기준의 나이는 20살

# def Taewoo(name, age):
    
#     if age >= 20:
#         print(f"{name}님은 성인입니다.")
        
#     elif age < 20 and age > 0: 
#         print(f"{name}님은 미성년자입니다.")
#     else:
#         print("잘못된 값을 입력했습니다.")



# name = input("이름을 입력하세요: ")
# age = int(input("나이를 입력하세요: "))


# Taewoo(name, age)

name = input('이름을 입력하세요:')
age = input('나이를 입력하세요:')


age1 = []

if len(age) == 1 :
    print(f"{name}님은 미성년자입니다.")
elif len(age) >= 2 :
    age1.append(age[0])
    age1.append(age[1])
    if age1[0] == "-" :
        print("잘못 입력했습니다.")
    elif int(age1[0]) >= 2:
        if int(age1[1]) >= 0:
            print(f"{name}님은 성인입니다.")
    elif int(age1[0]) < 2 :
        print(f"{name}님은 미성년자입니다.")