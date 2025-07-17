def solution(order):
    
    total = 0
    
    for item in order:                            #order는 문제의 조건에서 나와있듯이 빈 문자열 배열이다
        if item in ["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"]:
            total += 4500
            
        elif item in ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]:
            total += 5000
            
    return total






print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))

print(solution(["americanoice", "americano", "iceamericano"]))