print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for i in range(n): # 0부터 시작
  print('*', end='') # end: 끝에 들어가는 기본값 '\n'을 다른 문자로 치환
  if i % w == w - 1:
    print() # 줄바꿈 출력

if n % w:
  print() # 줄바꿈 출력