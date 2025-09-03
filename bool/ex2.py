# 논리 연산자로 조건식 만들기

# and : 둘 다 참이여야 결과가 참
print(True and True) #True
print(True and False) #False

# or : 하나라도 참이면 결과가 참
print(True or True) #True
print(True or False) #True

# 변수를 사용해서 조건식 만들기
age = 20 #나이
money = 10000 #소지금
# 나이가 20살 이상이고 소지금이 20000원 이상이면 참
print(age >= 20 and money >= 20000)

# not : 부정 연산자
# bool 값을 반대로 바꿈
print(not True)
