from typing import Sequence

def look_for_key(main_box: Sequence):
  pile = main_box.make_a_plie_to_look_through()
  while not pile.is_empty():
    box = pile.grab_a_box()
    for item in box:
      if item.is_a_box():
        pile.append(item)
      elif item.is_a_key():
        print('열쇠를 찾았어요!')

def look_for_key(box):
  for item in box:
    if item.is_a_box():
      look_for_key(item)
    elif item.is_a_key():
      print('열쇠를 찾았어요!')

