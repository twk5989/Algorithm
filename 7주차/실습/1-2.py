#https://school.programmers.co.kr/learn/courses/30/lessons/181894

def solution(arr):
    
    answer = []
    
    if 2 not in arr:
        
        return [-1]
    
    start = arr.index(2) 
             
    end = len(arr) - 1 - arr[::-1].index(2)   

    answer = arr[start:end+1]
    
    return answer

#end 인덱스를 찾는 방법에 있어서 arr[::-1].index(2)이렇게 뒤집어서 찾아야겠다는 생각은 있었다.
#근데 그 위치를 어떻게 나타내야 할지 모르겠어서 틀림.
#근데 잘 생각해보면 end의 위치에 대한 코드를 적을때에 대부분은 전체 배열의 길이에서 arr[::-1].index(2)이거를 더하거나 빼거나한다.
#이런 접근방식으로 조금 더 머리를 굴려서 하면 좋을 것 같다.
#그리고 index(2) = 3번째 요소의 값이지만 .index(2)는 요소들중 2의 요소가 어디에 있는지의 위치를 나타낸다