'''
* 다중 분기 조건문 if ~ elif ~ else
- 타 언어에서 else if로 작성하는 키워드를
파이썬에서는 단축해서 elif로 작성합니다.
문법의 의미는 똑같습니다.
- 첫번째 조건식의 결과가 False일 경우 아래에 있는
elif 문의 조건식을 새롭게 테스트하여 해당 조건이 True일 경우
elif에 종속된 코드를 실행합니다.
개수에 제한은 없습니다.
'''
age=int(input('나이: '))

if age>=20:
  print('성인입니다.')
elif age>=17:
  print('고딩')
elif age>=14:
  print('중딩')
elif age>=8:
  print('초딩')
else:
  print('꼬맹이입니다')



'''
* 중첩 if문
중첩 if문은 if블록 내부에 새로운 if문이
있는 형태입니다.
첫 번째 조건식의 결과가 True일 경우 한번 더 조건을 설정할 때
사용합니다.
'''

height=float(input('키 입력: '))
if height>=140:
  age=int(input('나이를 입력하세요: '))
  if age>=8:
    print('너 탑승가능!')
  else:
    print('나이가 8세 미만')
    print('너 NAGA')
else:
  print('키가 140미만!')
  print('너 NAGA')  






