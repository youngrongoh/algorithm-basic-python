def max_of(a):
  maximum = a[0]
  for i in range(1, len(a)): # 리스트 a 스캔
    if a[i] > maximum:
      maximum = a[i]
