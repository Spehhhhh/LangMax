from random import random
from math import floor

cards = [[1, 1], [0, 0], [1, 0]]
num_cards = len(cards)

N = 0  # Number of times first side is black
kk = 0  # Out of those, how many times the other side is white

for trial in range(int(1e6)):  # 1e6 is an arbitrary large number
    card = floor(num_cards * random())
    side = random() < 0.5
    other_side = int(not side)
    x1 = cards[card][side]
    x2 = cards[card][other_side]
    if x1 == 0:
        N += 1  # just seen another black face
        kk += x2 == 1  # count if other side was white

approx_probability = float(kk) / N
print(approx_probability)
