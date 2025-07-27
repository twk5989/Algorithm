# <리스트의 스캔>


#원소의 수를 len함수로 미리 알아내서 0에서 원소수 -1까지 반복한다
x = [1, 2, 3, 4]

for i in range(len(x)):
    print(f'x[{i}] = x[{i}]')
    
    
#인덱스와 원소를 짝지어서 enumerate함수로 반복해서 꺼낸다.
# enumerate함수 = 인덱스와 원소를 짝지어 튜플로 꺼내는 내장함수이다.
x = ['taewoo', 'wonjun', 'chanmin', 'seungwon', 'sokancha']
for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
    
    
#위의 실습과 같지만 1부터 카운트를 시작한다.0번째가 아닌 1번째로 출력된다.
x = ['taewoo', 'wonjun', 'chanmin', 'seungwon', 'sokancha']
for i, name in enumerate(x, 1):
    print(f'x{i}번째 = {name}')


#인덱스 값을 사용하지않고 in을 사용하여 원소를 처음부터 순서대로 꺼낸다.
x = ['taewoo', 'wonjun', 'chanmin', 'seungwon', 'sokancha']
for i in x:
    print(i)
    
#대부분 우리는 인덱스라는 번호표를 부여해서 원소를 할당한다. 근데 위의 코드는 인덱스를 건너뛰고 직접 모든 요소들을 i라는 변수에 할당시킴



# <튜플의 스캔>
#튜플은 [] -> () 이걸로 수정하면 스캔 할 수 있음

x = ('taewoo', 'wonjun', 'chanmin', 'seungwon', 'sokancha')