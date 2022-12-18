from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
  # 사용하는 쪽에서 idx 순서를 잘못 넣으면 의도대로 동작하지 않는다.
  # 1. 인자 이름을 left, mid, right 같이 명시적으로 짓는게 좋을 것 같다.
  # 2. mid는 내부에서 처리하는게 더 좋을 것 같다.
  if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
  if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
  if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
  return idx2

def sort3_improved(a: MutableSequence, left: int, right: int) -> None:
  if left > right: left, right = right, left
  mid = (left + right) // 2

  if a[mid] < a[left]: a[mid], a[left] = a[left], a[mid]
  if a[right] < a[mid]: a[mid], a[right] = a[right], a[mid]
  if a[mid] < a[left]: a[mid], a[left] = a[left], a[mid]

  return mid

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
  for i in range(left + 1, right + 1):
    j = i
    tmp = a[i]
    while j > 0 and a[j - 1] > tmp:
      a[j] = a[j - 1]
      j -= 1
    a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
  if right - left < 9:
    insertion_sort(a, left, right)
  else:
    pl = left
    pr = right
    m = sort3_improved(a, pl, pr)
    x = a[m]

    a[m], a[pr - 1] = a[pr - 1], a[m]
    pl += 1
    pr -= 1
    while pl <= pr:
      while a[pl] < x: pl += 1
      while a[pr] > x: pr -= 1
      if pl <= pr:
        a[pl], a[pr] = a[pr], a[pl]
        pl += 1
        pr -= 1
    
    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
  qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
  print('퀵 정렬을 합니다(원소 수가 9 미만이면 단순 삽입 정렬을 합니다.')
  num = int(input('원소 수를 입력하세요.: '))
  x = [None] * num

  for i in range(num):
    x[i] = int(input(f'x[{i}]: '))
  
  quick_sort(x)

  print('오름차순으로 정렬했습니다.')
  for i in range(num):
    print(f'x[{i}] = {x[i]}')

