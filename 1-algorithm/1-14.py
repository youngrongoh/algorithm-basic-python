print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for i in range(n):
  print('*', end='')
  if i % w == w - 1:
    print() # 줄바꿈 출력

if n % w:
  print() # 줄바꿈 출력