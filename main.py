from random import choice
from itertools import product

suits = ("multi", "rosso", "verde")
values = [14] + [12]*2

deck = dict(zip(suits, values))
display = dict(zip(suits, [0]*3))

def pick(suits, deck, display):
  c = choice(suits)
  deck[c] -= 1
  display[c] += 1
  print(deck)
  print(display)
  
suits2 = ("bastoni", "coppe", "spade", "denari")
values2 = range(1, 11)

deck2 = set((x, y) for x in suits for y in values if x != y) 
display2 = set()
display2.add(deck2.pop())
print(display2)

