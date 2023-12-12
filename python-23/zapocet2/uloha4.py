# Na vstupe sú čísla oddelené čiarkami.
# Vytvorte zoznam kladných čísel a zoznam záporných čísel - poradie čísel ponechajte ako v zadaní. Výsledok vypíšte v poradí kladné, záporné.
# Vstup: 1,8,3,5,-8,9,-7,5,-3,-9
# Výstup:
# kladné: [1, 8, 3, 5, 9, 5]
# záporné: [-8, -7, -3, -9]


user_input = input().split(",")
kladne = []
zaporne = []

for num in user_input:
  if int(num) < 0:
    zaporne.append(num)
  else:
    kladne.append(num)

kladne = list(map(int, kladne))
zaporne = list(map(int, zaporne))
    
print(f"kladné: {kladne}")
print(f"záporné: {zaporne}")