'''
* 리스트의 내부 요소 다루기
- 리스트는 시퀀스 자료형이기 때문에 인덱스를 통한
요소들의 관리가 가능합니다.
- 리스트를 다룰 때는 문자열과 비슷한 방식을 사용합니다.
'''
foods=['짜장면','탕수육','삼겹살','족발','피자']
print(foods[2])
print(foods[1][2])
print(foods[0][:2])

#리스트 슬라이싱 ->리스트데이터[begin:end:step]

nums=[0,1,2,3,4,5,6,7,8,9]

print(nums[2:5:1])
print(nums[:4])
print(nums[1:7:2])

# 리스트는 인덱싱을 사용하여 변수처럼 내부의 값을 변경하는 것이 자유롭습니다.

print('-'*40)
print(nums)

nums[2]=34
print(nums)

nums[3]=nums[6]
print(nums)


s='python'
#s[2]= 'x'


#unpacraging: 




