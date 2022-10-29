n = 1
def put_id():
  x = 1
  print(f"id(x) = {id(x)}") #id는 변수 내 인자를 객체로 취급하여 고유 값을 리턴한다.

print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()