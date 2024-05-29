'''
* 튜플 (tuple)
- 튜플은 값의 집합이라는 측면에서는 리스트와 유사하지만
값을 한 번 저장한 후에는 내부 요소의 편집이 불가능합니다.
- 튜플은 상수 리스트라고도 부르며 ()를 사용하여 표현합니다.
- 튜플도 문자열과 리스트와 마찬가지로 시퀀스 자료형 입니다. (인덱스 o)
'''

points= (87,97,23,45,100)
print(type(points))

sum=0
for p in points:
  sum+=p
print(f'총점: {sum}점, 평균: {sum/len(points):0.1f}점')  

#튜플을 만들 때는 ()를 생략할 수 있습니다.
print('-'*40)
tu=1,3,5,7,9
print(type(tu))

# 튜플은 리스트와 마찬가지로 unpackaging이 가능합니다.
n1,n2,n3,n4,n5 = tu
print(n1,n2,n3,n4,n5)

#튜플로 가능한 문법 (내부 요소값을 바꾸지 않는 행위)
print(tu[2])
print(tu[1:3])
print(tu+(10,11))
print(tu*2)
print(tu)


#튜플로 불가능한 문법(내부 요소값을 바꾸는 행위)
#tu[2]=19 (x)
# tu.append(10)(x)
#del tu[0] (x)

#튜플이 지원하는 메서드는 index(),count() 뿐입니다.

'''
* 튜플을 사용하는 이유

- 튜플로 가능한 일은 리스트로도 모두 가능합니다.
 리스트는 튜플에 비해 요소를 편집하는 행위도 가능합니다.

- 결국, 리스트는 튜플의 기능을 모두 포괄하는 더 큰 범위의
타입이지만, 튜플을 사용해야 하는 이유는 존재합니다.

1. 비용의 차이: 리스트는 변경의 가능성을 항상 대비해야 하기 때문에
더 많은 메모리 공간을 차지하고, 속도도 그만큼 느립니다.
이에 비해, 튜플은 값의 집합만 표현할 뿐, 바뀔 일이 없으므로
내부 구조가 더 단순하고 속도도 더 빠릅니다.

2. 데이터 안정성: 리스트는 실수로 내부 데이터가 의도치 않게
 바뀔 위험이 있지만, 튜플은 한 번 정해지면 바뀔 수가 없기 때문에
 실수할 위험이 적습니다.

데이터베이스나 네트워크에서 얻은 데이터는 단순히 참조만 하면
될 뿐, 편집할 일이 많지 않습니다.
그렇기 때문에 리스트로 관리하는 것보다 튜플로 처리하는 것이
안전합니다.

3. 리스트와 상호 변경이 자유로움: 리스트와 튜플은
값 변경 가능성 여부만 다를 뿐, 구조가 상당히 유사합니다.
리스트를 튜플로 변환할 때는 내장함수 tuple()을 사용하고,
튜플을 리스트로 변환할 때는 내장함수 list()를 사용합니다.
'''

print('-'*40)
p=[2,3,4,5,6]

p=tuple(p)
#p[1]=6 튜플에서는 값의 변경이 불가능

p=list(p)

p[3]=100
p.append(17)
print(p)



