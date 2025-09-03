weather = '맑음' # 맑음, 비, 눈

# 앞에 조건이 참이면, 다음 조건 판단하지 않음
# 모든 조건 거짓 -> else 블록 수행
if weather == '비':
    print('우산을 가져간다.')
elif weather == '눈':
    print('장화를 신는다.')
else:
    print('우산을 가져가지 않는다.')

