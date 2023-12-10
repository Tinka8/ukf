# we move in square board. We move N (north), S (south), E (east), W (west).
# we start from (0,0), as input we get string with moves, for example:
# moves = "NENW" or moves = "NNEESSWW" or moves = "NNEESSWWNNEESSWW"
# and as result we want to get shortest path to get back to (0,0)
# first horizontal, then vertical

moves = str(input())

x = 0
y = 0


for move in moves:
    if move == "N":
        y -= 1
    elif move == "S":
        y += 1
    elif move == "E":
        x -= 1
    elif move == "W":
        x += 1


if (x == 0 and y == 0):
    print("si doma")
    exit()


if (x > 0):
    print("E" * x, end="")
else:
    print("W" * abs(x), end="")

if (y > 0):
    print("N" * y, end="")
else:
    print("S" * abs(y), end="")


print()