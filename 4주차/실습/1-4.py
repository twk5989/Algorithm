
def solution(arr, flag):   #arr, flag를 매개변수로 받는 함수를 일단 정의
    X = [] #배열 X를 빈 리스트로 초기화

    for i in range(len(arr)):  #arr의 길이만큼 반복하는 반복문이겠지
        
        if flag[i]:             #flag가 True일때
            X += [arr[i]] * (arr[i] * 2)
            
        else:                   #False
            X = X[:-arr[i]]   #python의 슬라이싱 문법

    return X



#슬라이싱 문법
# [start:stop:step]원칙을 따른다. 여기서는 start 생략 즉 처음부터 끝에서 arr[i]전까지. step은 생략(1)씩 자른 나머지를 출력해라
#stop이 음수면 뒤에서 부터 시작이고 양수면 앞에서부터이다. 그리고 step이 기본값 1이면 앞으로, -음수이면 뒤로
#X[:arr[i]]면 앞에서부터 세는 거임X = [10, 20, 30, 40, 50] arr_i = 3 print(X[:arr_i]) 3번째전까지 자르기 자른다는 말은 남긴다는것
#X = X[:-arr[i]]이거는 처음부터~뒤에서 arr[i]까지 자른다인거고













arr = [3, 2, 4, 1, 3]
flag = [True, True, False, True, False]

# i=0: True → X += [3]*6 → X = [3,3,3,3,3,3]
# i=1: True → X += [2]*4 → X = [3,3,3,3,3,3,2,2,2,2]
# i=2: False → X에서 4개 제거 → X = [3,3,3,3,3,3]
# i=3: True → X += [1]*2 → X = [3,3,3,3,3,3,1,1]
# i=4: False → X에서 3개 제거 → X = [3,3,3,3,3]

print(solution(arr, flag))  # 최종결과: [3, 3, 3, 3, 3]
