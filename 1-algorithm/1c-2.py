# 가독성이 떨어진다.
# 오름차이든 내림차이든 크기순으로 정렬한 뒤에 인덱스로 가운데 값을 가져오는게 좋을 것 같다.
def med(a, b, c):
  # (c <= a <= b) or (b <= a <= c)
  if (b >= a and c <= a) or (b <= a and c >= a):
    return a
  # (c < b < a) or (a < b < c)
  if (a > b and c < b) or (a < b and c > b):
    return b
  # (a < c < b) or (b < c < a)
  return c

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med(a, b, c)}입니다.')