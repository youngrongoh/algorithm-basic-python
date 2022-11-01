items = [
  { 'key': 'a1', 'value': 1 },
  { 'key': 'a2', 'value': 2 },
  { 'key': 'a3', 'value': 3 },
  { 'key': 'a4', 'value': 4 },
  { 'key': 'a5', 'value': 5 },
  { 'key': 'a6', 'value': 6 },
  { 'key': 'a7', 'value': 7 },
  { 'key': 'a8', 'value': 8 },
]
ss = [item['key'] for item in items if item['value'] > 3]

print(ss)