import random

n = int(input('난수의 개수를 입력하세요.: '))

for _ in range(n):
  r = random.randint(10, 99)
  print(r, end='')
  if r == 13:
    print('\n프로그램을 중단합니다.')
    break
else: # 반복이 끝난 후 실행 / break문으로 인한 종료 시에는 실행되지음않음
  print('\n난수 생성을 종료합니다.')
