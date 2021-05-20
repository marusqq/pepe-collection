photos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

from itertools import combinations
ph = combinations(photos, 2)

print(list(ph))