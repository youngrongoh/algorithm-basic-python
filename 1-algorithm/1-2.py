def max(a, b, c):
  maximum = a
  if b > maximum: maximum = b
  if c > maximum: maximum = c
  return maximum

print(f'max(3, 2, 1) = {max(3, 2, 1)}')
print(f'max(3, 2, 2) = {max(3, 2, 2)}')
print(f'max(3, 1, 2) = {max(3, 1, 2)}')
print(f'max(3, 2, 3) = {max(3, 2, 3)}')
print(f'max(3, 1, 3) = {max(3, 1, 3)}')
print(f'max(2, 1, 3) = {max(2, 1, 3)}')
print(f'max(3, 3, 2) = {max(3, 3, 2)}')
print(f'max(3, 3, 3) = {max(3, 3, 3)}')
print(f'max(2, 2, 3) = {max(2, 2, 3)}')
print(f'max(2, 3, 1) = {max(2, 3, 1)}')
print(f'max(2, 3, 2) = {max(2, 3, 2)}')
print(f'max(2, 3, 3) = {max(2, 3, 3)}')
print(f'max(1, 2, 3) = {max(1, 2, 3)}')