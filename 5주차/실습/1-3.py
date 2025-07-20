# 문제 설명
# 정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 6 ≤ num_list의 길이 ≤ 30
# 1 ≤ num_list의 원소 ≤ 100

# 입출력 예
# num_list	result
# [12, 4, 15, 46, 38, 1, 14, 56, 32, 10]	[15, 32, 38, 46, 56]



def solution(num_list):
    if len(num_list) < 6 or len(num_list) > 30:  #찬민아 드모르간 사용했어 질문하지마
        print ("num_list의 길이는 6 이상 30 이하여야 합니다.")
    return [None]
    
    sorted_list = sorted(num_list) #오름차순으로
    
    answer = sorted_list[5:]  #앞에서 5개 남겨두고 지움

    return answer

print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))
print(solution([1, 2, 3]))
